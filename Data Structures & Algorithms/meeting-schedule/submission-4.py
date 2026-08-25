"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda interval: interval.start)
        res = [intervals[0].end]

        for interval in intervals[1:]:
            lastEnd = res[-1]
            if interval.start < lastEnd:
                return False
            else:
                res.append(interval.end)
        return True
