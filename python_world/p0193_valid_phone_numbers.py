import re


PHONE_PATTERN = re.compile(r"^(?:\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$")


def valid_phone_numbers(text: str) -> list[str]:
    """Python equivalent of the line-filtering shell command in problem 193."""
    return [line for line in text.splitlines() if PHONE_PATTERN.fullmatch(line)]

