from __future__ import annotations


def second_highest_salary(salaries: list[int]) -> int | None:
    """Python equivalent of the SQL query in LeetCode problem 176."""
    distinct = sorted(set(salaries), reverse=True)
    return distinct[1] if len(distinct) > 1 else None
