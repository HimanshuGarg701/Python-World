from __future__ import annotations


class Solution:
    _BELOW_TWENTY = (
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen",
    )
    _TENS = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
    _SCALES = ((1_000_000_000, "Billion"), (1_000_000, "Million"), (1_000, "Thousand"))

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        words: list[str] = []
        for value, name in self._SCALES:
            if num >= value:
                words.extend(self._under_thousand(num // value))
                words.append(name)
                num %= value
        words.extend(self._under_thousand(num))
        return " ".join(words)

    def _under_thousand(self, number: int) -> list[str]:
        words: list[str] = []
        if number >= 100:
            words.extend((self._BELOW_TWENTY[number // 100], "Hundred"))
            number %= 100
        if number >= 20:
            words.append(self._TENS[number // 10])
            number %= 10
        if number:
            words.append(self._BELOW_TWENTY[number])
        return words
