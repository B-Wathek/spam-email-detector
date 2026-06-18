# Tool allowlist and basic security checks

ALLOWED_TOOLS = {
    "predict",
    "train",
    "evaluate"
}

def validate_tool(tool_name: str):
    """
    Ensures only allowed tools can be used.
    """
    if tool_name not in ALLOWED_TOOLS:
        raise ValueError(f"Tool not allowed: {tool_name}")
