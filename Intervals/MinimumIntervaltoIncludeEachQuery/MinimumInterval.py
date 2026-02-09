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

# Optimal Solution
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        bookkeeping = {}
        lastInterval = []
        n = len(intervals)
        start = 0
        for query in sorted(queries):
            mini = -1
            while start < n:
                if intervals[start][0] <= query and query <= intervals[start][1]:
                    heapq.heappush(lastInterval, (intervals[start][1] - intervals[start][0] + 1, intervals[start][1]))
                elif intervals[start][0] > query:
                    break
                start+=1

            while lastInterval:
                if query <= lastInterval[0][1]:
                    mini = lastInterval[0][0]
                    break
                else:
                    heapq.heappop(lastInterval)

            bookkeeping[query] = mini
        return [bookkeeping[query] for query in queries]