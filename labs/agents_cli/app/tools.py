import os
import ast

DATA_PATH = os.path.join("data", "local_docs.txt")


def search_docs(query: str) -> str:
    if not os.path.exists(DATA_PATH):
        return "Document file not found."

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if query.lower() in content.lower():
        return content[:1500]
    return "No relevant information found."


def calculator(expression: str) -> str:
    try:
        result = eval(compile(ast.parse(expression, mode="eval"), "<string>", "eval"), {"__builtins__": {}})
        return str(result)
    except Exception:
        return "Invalid mathematical expression."


def summarize(text: str) -> str:
    return text[:300] + "..." if len(text) > 300 else text