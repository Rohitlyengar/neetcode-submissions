"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key = lambda interval: (interval.start, interval.end))

        heap = []
        for interval in intervals:
            if heap and interval.start < heap[0]:
                heapq.heappush(heap, interval.end)
            else:
                if heap:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
        return len(heap)
