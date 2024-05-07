def employees_earning_more_than_managers(
    employees: list[dict[str, object]],
) -> list[str]:
    """Python equivalent of the SQL self-join in LeetCode problem 181."""
    by_id = {employee["id"]: employee for employee in employees}
    result: list[str] = []
    for employee in employees:
        manager = by_id.get(employee.get("managerId"))
        if manager and employee["salary"] > manager["salary"]:
            result.append(str(employee["name"]))
    return result

