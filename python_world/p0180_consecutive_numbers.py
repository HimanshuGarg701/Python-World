def consecutive_numbers(logs: list[tuple[int, int]]) -> list[int]:
    """Python equivalent of the SQL consecutive-row query in problem 180."""
    values = [number for _, number in sorted(logs)]
    return sorted({values[index] for index in range(2, len(values)) if len(set(values[index - 2 : index + 1])) == 1})
