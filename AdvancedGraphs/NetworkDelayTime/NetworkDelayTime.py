class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dictionary of Dictionarys
        # source : (target : cost)
        costs = defaultdict(dict)
        visited = set()
        for time in times:
            costs[time[0]][time[1]] = time[2]

        queue = []
        heapq.heappush(queue, (0, k))
        result = 0
        while queue:
            curr = heapq.heappop(queue)
            if curr[1] in visited: continue
            visited.add(curr[1])
            for nei in costs[curr[1]]:
                if nei not in visited:
                    heapq.heappush(queue, (costs[curr[1]][nei] + curr[0], nei))
            result = curr[0]
        return result if len(visited) == n else -1