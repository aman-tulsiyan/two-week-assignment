import json
from pydantic import ValidationError

from app.config import client, MAX_STEPS, MODEL_NAME
from app.schema import ToolCall
from app.tools import search_docs, calculator, summarize


# Guardrail: Tool whitelist
ALLOWED_TOOLS = {
    "search_docs": search_docs,
    "calculator": calculator,
    "summarize": summarize,
}


def run_agent(user_query: str) -> str:
    messages = [
                {
            "role": "system",
            "content": (
                "You are a tool-using agent.\n\n"
                "You have access to ONLY these tools:\n"
                "1. search_docs(query: str) — searches local document file called local_docs.txt\n"
                "2. calculator(expression: str) — evaluates math expressions\n"
                "3. summarize(text: str) — summarizes a given text\n\n"
                "Whenever the user asks about information in the documents, use 'search_docs'.\n"
                "After retrieving text, you may call 'summarize' to shorten it.\n\n"
                "Always respond ONLY in JSON format when calling a tool:\n"
                '{"tool_name": "<exact_tool_name>", "arguments": {...}}\n'
                "Do NOT respond in plain text when a tool is needed.\n"
                "Only respond in plain text as the final answer if no tools are needed."
            )
        },
        {"role": "user", "content": user_query}, 
    ]

    for step in range(MAX_STEPS):
        print(f"\n--- Step {step + 1} ---")

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0,# temp is set as zero for deterministic results 
        )

        content = response.choices[0].message.content
        print("Model Output:", content)

        # Try validating as tool call
        try:
            tool_call = ToolCall.model_validate_json(content)
        except ValidationError:
            return "Final Answer:\n" + content

        # Guardrail: Whitelist enforcement
        if tool_call.tool_name not in ALLOWED_TOOLS:
            return "Error: Tool not allowed."

        tool_function = ALLOWED_TOOLS[tool_call.tool_name]

        try:
            result = tool_function(**tool_call.arguments)
        except Exception as e:
            result = f"Tool execution error: {str(e)}"

        # Add tool call + result to memory
        messages.append({"role": "assistant", "content": content})
        messages.append({"role": "user", "content": f"Tool result: {result}\nContinue."})

    return "Error: Max steps reached."