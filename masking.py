import re
def mask_sensitive_data(text):
    text = re.sub(
        r"(password\s*=\s*)(.+)",
        r"\1********",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"(api[_-]?key\s*=\s*)(.+)",
        r"\1********",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"(Bearer\s+)(\S+)",
        r"\1********",
        text,
        flags=re.IGNORECASE
    )

    return text