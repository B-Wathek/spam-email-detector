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

    return True


def validate_input(text: str):
    """
    Basic parameter validation.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be string")

    if len(text) > 10000:
        raise ValueError("Input too long")

    if text.strip() == "":
        raise ValueError("Input cannot be empty")

    return True
