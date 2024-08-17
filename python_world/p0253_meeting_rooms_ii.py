from __future__ import annotations

import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval[0])
        end_times: list[int] = []
        for start, end in intervals:
            if end_times and end_times[0] <= start:
                heapq.heapreplace(end_times, end)
            else:
                heapq.heappush(end_times, end)
        return len(end_times)
