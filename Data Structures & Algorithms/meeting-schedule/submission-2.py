"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Overlap checker
        def overlaps(interval_1, interval_2):
            if interval_1.start == interval_2.start and interval_1.end == interval_2.end:
                return True
            if interval_2.start < interval_1.start < interval_2.end:
                return True
            if interval_2.start < interval_1.end < interval_2.end:
                return True
            if interval_1.start < interval_2.start < interval_1.end:
                return True
            if interval_1.start < interval_2.end < interval_1.end:
                return True
            return False

        # Sort according to start time
        intervals.sort(key = lambda x: x.start)

        # Check conflicts
        for i in range(1, len(intervals)):
            if overlaps(intervals[i-1], intervals[i]):
                return False
        return True

        

