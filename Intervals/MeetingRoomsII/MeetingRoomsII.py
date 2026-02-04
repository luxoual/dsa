# Bruteforce (DFS Backtracking)
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n <= 1:
            return n
        intervals.sort(key = lambda i: i.start)
        # day = (s, e)
        # a new interval fits if its end <= s or start >= e
        # and after adding an interval
        # day = (min(s,new_s), max(e, new_e))
        result = float('inf')
        days = []
        def dfs(i):
            nonlocal result
            if i == n:
                result = min(result, len(days))
                return
            
            # Traversal
            d = len(days)
            if d > result: return
            # Add into any open days
            for j in range(d):
                if intervals[i].start >= days[j][1]:
                    # Addable
                    temp = days[j][1]
                    days[j] = (days[j][0], max(intervals[i].end, days[j][1]))
                    dfs(i+1)
                    days[j] = (days[j][0], temp)
            
            # Start new day
            days.append((intervals[i].start, intervals[i].end))
            dfs(i+1)
            days.pop()
        
        dfs(0)
        return result
    
# Sorting + Min-Heap Solution O(n log n) time, O(n) space
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Using the concept we learned from NonOverlappingIntervals
        # We always want to keep or take the timeline with the earliest
        # ending time, becaus it leaves more space for more meetings.
        # sorting by start, any non-overlapping intervals go into the same
        # room, all we have ot hceck is if the start >= the current end
        # of a room. If it overlaps, we can start a new room, and we always
        # try fitting the interval into the earliest ending room,
        # if it doesnt fit in the earliest endign room, it wont fit in
        # any rooms that end later than it

        # We sort by start, because we have to process the intervals
        # sequentially like how time flows, any intervals we end up
        # at will start after the previous ones
        n = len(intervals)
        if n <= 1:
            return n
        intervals.sort(key = lambda i: i.start)
        rooms = [intervals[0].end]

        for i in range(1, n):
            interval = intervals[i]
            if interval.start >= rooms[0]:
                # It fits, so replace 
                heapq.heappop(rooms)
            # It overlaps, so we start a new one
            # Both times we push it in
            heapq.heappush(rooms, interval.end)
        
        return len(rooms)