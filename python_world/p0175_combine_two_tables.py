def combine_two_tables(
    people: list[dict[str, object]], addresses: list[dict[str, object]]
) -> list[dict[str, object]]:
    """Python equivalent of the SQL left join used by LeetCode problem 175."""
    by_person = {row["personId"]: row for row in addresses}
    return [
        {
            "firstName": person["firstName"],
            "lastName": person["lastName"],
            "city": by_person.get(person["personId"], {}).get("city"),
            "state": by_person.get(person["personId"], {}).get("state"),
        }
        for person in people
    ]

