from collections import Counter


class TwoSum:
    def __init__(self):
        self.counts: Counter[int] = Counter()

    def add(self, number: int) -> None:
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        for number, count in self.counts.items():
            complement = value - number
            if complement != number and complement in self.counts:
                return True
            if complement == number and count > 1:
                return True
        return False

