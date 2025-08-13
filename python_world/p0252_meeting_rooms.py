from __future__ import annotations


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda interval: interval[0])
        return all(
            intervals[index - 1][1] <= intervals[index][0]
            for index in range(1, len(intervals))
        )
