from __future__ import annotations

from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from typing import Any


def trips_and_users(
    trips: list[dict[str, Any]], users: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    eligible = {user["users_id"] for user in users if user["banned"] == "No"}
    totals: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for trip in trips:
        day = trip["request_at"]
        if not "2013-10-01" <= day <= "2013-10-03":
            continue
        if trip["client_id"] not in eligible or trip["driver_id"] not in eligible:
            continue
        totals[day][0] += 1
        if trip["status"] != "completed":
            totals[day][1] += 1
    result: list[dict[str, Any]] = []
    for day in sorted(totals):
        total, cancelled = totals[day]
        rate = (Decimal(cancelled) / Decimal(total)).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        result.append({"Day": day, "Cancellation Rate": float(rate)})
    return result
