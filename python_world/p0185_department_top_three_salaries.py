def department_top_three_salaries(
    employees: list[dict[str, object]], departments: list[dict[str, object]]
) -> list[dict[str, object]]:
    """Python equivalent of the dense-rank SQL query in LeetCode problem 185."""
    department_names = {department["id"]: department["name"] for department in departments}
    top: dict[object, set[object]] = {}
    for employee in employees:
        department_id = employee["departmentId"]
        top.setdefault(department_id, set()).add(employee["salary"])
    allowed = {
        department_id: set(sorted(salaries, reverse=True)[:3])
        for department_id, salaries in top.items()
    }
    return [
        {
            "Department": department_names[employee["departmentId"]],
            "Employee": employee["name"],
            "Salary": employee["salary"],
        }
        for employee in employees
        if employee["salary"] in allowed[employee["departmentId"]]
    ]

