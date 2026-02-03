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