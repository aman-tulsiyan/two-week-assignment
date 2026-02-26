# agent.py

from tools import ALLOWED_TOOLS
from schema import validate_summary

MAX_STEPS = 5


def agent_loop(user_query: str):
    steps = 0
    context = user_query

    while steps < MAX_STEPS:
        steps += 1

        # I will Replace this with the LLM Later(just a prototype(basic version)) 
        if "calculate" in context:
            tool_name = "compute"
            tool_input = context.replace("calculate", "").strip()

        elif "search" in context:
            tool_name = "search_docs"
            tool_input = context.replace("search", "").strip()

        else:
            tool_name = "write_summary"
            tool_input = context

        #  Tool whitelist check
        if tool_name not in ALLOWED_TOOLS:
            raise Exception("Tool not allowed")

        result = ALLOWED_TOOLS[tool_name](tool_input)

        # If summary, validate and return
        if tool_name == "write_summary":
            validate_summary(result)
            return result

        # Otherwise continue loop with new context
        context = result

    raise Exception("Max steps exceeded")