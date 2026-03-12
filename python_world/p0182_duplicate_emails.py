from collections import Counter


def duplicate_emails(emails: list[str]) -> list[str]:
    """Python equivalent of the SQL grouping query in LeetCode problem 182."""
    counts = Counter(emails)
    return sorted(email for email, count in counts.items() if count > 1)

