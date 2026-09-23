def department_highest_salary(
    employees: list[dict[str, object]], departments: list[dict[str, object]]
) -> list[dict[str, object]]:
    """Python equivalent of the SQL grouped-maximum query in problem 184."""
    department_names = {department["id"]: department["name"] for department in departments}
    maxima: dict[object, object] = {}
    for employee in employees:
        department_id = employee["departmentId"]
        maxima[department_id] = max(maxima.get(department_id, employee["salary"]), employee["salary"])
    return [
        {
            "Department": department_names[employee["departmentId"]],
            "Employee": employee["name"],
            "Salary": employee["salary"],
        }
        for employee in employees
        if employee["salary"] == maxima[employee["departmentId"]]
    ]

