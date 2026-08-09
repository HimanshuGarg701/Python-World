class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        whole, remainder = divmod(numerator, denominator)
        if remainder == 0:
            return sign + str(whole)
        digits: list[str] = []
        positions: dict[int, int] = {}
        while remainder and remainder not in positions:
            positions[remainder] = len(digits)
            digit, remainder = divmod(remainder * 10, denominator)
            digits.append(str(digit))
        if remainder:
            start = positions[remainder]
            digits.insert(start, "(")
            digits.append(")")
        return f"{sign}{whole}." + "".join(digits)

