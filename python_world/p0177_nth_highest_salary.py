from __future__ import annotations


def nth_highest_salary(salaries: list[int], n: int) -> int | None:
    """Python equivalent of the SQL function in LeetCode problem 177."""
    distinct = sorted(set(salaries), reverse=True)
    return distinct[n - 1] if 1 <= n <= len(distinct) else None
