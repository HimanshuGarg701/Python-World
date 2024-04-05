def customers_who_never_order(
    customers: list[dict[str, object]], orders: list[dict[str, object]]
) -> list[str]:
    """Python equivalent of the SQL anti-join in LeetCode problem 183."""
    ordered = {order["customerId"] for order in orders}
    return [str(customer["name"]) for customer in customers if customer["id"] not in ordered]

