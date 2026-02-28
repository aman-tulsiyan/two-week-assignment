# schema.py

from pydantic import BaseModel

class ToolCall(BaseModel):
    tool_name: str
    arguments: dict