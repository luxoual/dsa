# Bruteforce
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = []
        intervals.sort()
        print(intervals)
        for query in queries:
            print(query)
            mini = float('inf')
            for interval in intervals:
                if interval[0] <= query and query <= interval[1]: # Make sure to stay in range
                    mini = min(mini, interval[1] - interval[0] + 1)
                elif interval[0] > query:
                    break
            if mini == float('inf'):
                mini = -1
            result.append(mini)
        
        return result