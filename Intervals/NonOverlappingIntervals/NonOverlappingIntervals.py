# Initial Solution - Sorting by Start Time
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Ok so overlapping is when one interval overlaps with
        # another interval, and it isn't a common point
        # a common point is when a start of one interval is the
        # same as the end of another interval

        # Hint 1
        # Overlapping intervals is also if two intervals
        # are sorted (ascending) and the 2nd start value is
        # less than the 1st end value

        # One of the two is the one we need to remove, so 
        # lets remove the one with the lower end value
        intervals.sort()
        left = 0
        right = 1
        result = 0
        while right < len(intervals):
            # Check if right is overlapping with the left
            if intervals[right][0] < intervals[left][1]:
                # We have an overlap, so choose the one with the shorter end
                if intervals[left][1] > intervals[right][1]:
                    left = right
                result+=1
            # If it doesn't overlap, then we can move
            else:
                left = right
            right+=1

        return result
        
# Optimized Solution - Sorting by End Time
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Hint 1
        # Overlapping intervals is also if two intervals
        # are sorted (ascending) and the 2nd start value is
        # less than the 1st end value

        # One of the two is the one we need to remove, so 
        # lets remove the one with the lower end value

        # Sort by ending time, because we always want the interval
        # with the smallest ending time, then as we go we just need
        # to see if any start times are less than this current ending
        # if its less than it, then it overlaps and we get rid of it
        # if it doesn't, then we have to update the ending
        # Since its sorted, we don't gotta worry about any endings
        # that come in between or before the current ending we are tracking
        intervals.sort(key = lambda interval: interval[1])
        result = 0
        currEnd = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < currEnd:
                # Overlaps
                result+=1
            else:
                # Doesn't overlap, so we replace currEnd
                # because we are adding it to our timeline
                currEnd = interval[1]

        return result
        
        

