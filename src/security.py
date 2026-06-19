ALLOWED_TOOLS = [
    "spam_classifier",
    "email_parser"
]

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be string")

    if len(text) > 10000:
        raise ValueError("Input too long")

    return True
