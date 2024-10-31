class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for index, (available, required) in enumerate(zip(gas, cost)):
            tank += available - required
            if tank < 0:
                start = index + 1
                tank = 0
        return start

