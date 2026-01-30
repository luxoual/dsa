# Bruteforce
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Bruteforce, with every meeting, we check if theres
        # a conflict with every other meeting. If we find
        # at least one conflict, we return false

        n = len(intervals)
        for i in range(n):
            for j in range(i+1, n):
                if (intervals[i].end > intervals[j].start and intervals[i].start <= intervals[j].start) or (intervals[j].end > intervals[i].start and intervals[j].start <= intervals[i].start):
                    return False
        
        return True

# Sorting Solution O(n log n) time, O(1) space

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # We are looking for no overlapping time slots
        # if we find an overlap, we can return False
        # An overlap would be when the start of one timeslot
        # is before the end of another timeslot, and the other
        # timeslot also starts before the first timeslot

        intervals.sort(key=lambda interval:interval.start)
        for i in range(1, len(intervals)):
            # If the start is before the end of the first interval
            if intervals[i].start < intervals[i-1].end:
                return False

        return True