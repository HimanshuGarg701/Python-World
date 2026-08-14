class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result: list[str] = []

        def search(index: int, expression: str, total: int, previous: int) -> None:
            if index == len(num):
                if total == target:
                    result.append(expression)
                return
            for end in range(index + 1, len(num) + 1):
                if end > index + 1 and num[index] == "0":
                    break
                token = num[index:end]
                value = int(token)
                if index == 0:
                    search(end, token, value, value)
                else:
                    search(end, expression + "+" + token, total + value, value)
                    search(end, expression + "-" + token, total - value, -value)
                    search(end, expression + "*" + token,
                           total - previous + previous * value, previous * value)

        search(0, "", 0, 0)
        return result
