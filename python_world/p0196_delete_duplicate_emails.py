def delete_duplicate_emails(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Python equivalent of the SQL delete in LeetCode problem 196."""
    lowest_id: dict[object, object] = {}
    for row in rows:
        email = row["email"]
        lowest_id[email] = min(lowest_id.get(email, row["id"]), row["id"])
    return [row for row in rows if row["id"] == lowest_id[row["email"]]]

