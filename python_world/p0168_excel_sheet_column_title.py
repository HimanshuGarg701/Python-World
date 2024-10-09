class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title: list[str] = []
        while columnNumber:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            title.append(chr(ord("A") + remainder))
        return "".join(reversed(title))

