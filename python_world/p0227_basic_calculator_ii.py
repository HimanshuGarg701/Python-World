class Solution:
    def calculate(self, s: str) -> int:
        stack: list[int] = []
        number = 0
        operation = "+"
        for index, character in enumerate(s):
            if character.isdigit():
                number = number * 10 + int(character)
            if character in "+-*/" or index == len(s) - 1:
                if operation == "+":
                    stack.append(number)
                elif operation == "-":
                    stack.append(-number)
                elif operation == "*":
                    stack[-1] *= number
                else:
                    stack[-1] = int(stack[-1] / number)
                operation = character
                number = 0
        return sum(stack)
