class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
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
