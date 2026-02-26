import os
import math

# 1️⃣ Search Local Docs
def search_docs(query: str) -> str:
    results = []
    for root, _, files in os.walk("docs"):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if query.lower() in content.lower():
                        results.append(content[:1000])
    return "\n".join(results) if results else "No results found."


# 2️⃣ Safe Compute
SAFE_GLOBALS = {
    "__builtins__": {},
    "math": math
}

def compute(expression: str) -> str:
    try:
        result = eval(expression, SAFE_GLOBALS)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


# 3️⃣ Write Summary (LLM placeholder)
def write_summary(data: str) -> dict:
    # Replace with real LLM call later
    return {
        "title": "Summary",
        "key_points": data.split("\n")[:3]
    }


# 🔐 Tool Whitelist
ALLOWED_TOOLS = {
    "search_docs": search_docs,
    "compute": compute,
    "write_summary": write_summary
}