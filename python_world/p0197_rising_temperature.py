from datetime import date, timedelta


def rising_temperature(weather: list[dict[str, object]]) -> list[object]:
    """Python equivalent of the date self-join in LeetCode problem 197."""
    by_date: dict[date, dict[str, object]] = {}
    for row in weather:
        recorded = row["recordDate"]
        day = recorded if isinstance(recorded, date) else date.fromisoformat(str(recorded))
        by_date[day] = row
    result: list[object] = []
    for day, row in by_date.items():
        previous = by_date.get(day - timedelta(days=1))
        if previous and row["temperature"] > previous["temperature"]:
            result.append(row["id"])
    return result

