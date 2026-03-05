# Dijkstra's Algorithm
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
    
# DFS solution
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DFS
        adj = defaultdict(dict)
        shortest = [float('inf')] * n
        for time in times:
            adj[time[0]][time[1]] = time[2]
        
        # i represents what node we are on, and prev
        # represents how much we have travelled so far
        # to get here
        def dfs(i, prev):
            # Basecase
            # We are going for the shortest path, so
            # if we get anything that is greater than
            # our currently stored shortest path, then
            # we don't even continue, so we also don't
            # need to worry about loops
            if prev >= shortest[i-1]: return

            shortest[i-1] = prev
            # Else we traverse
            for nei in adj[i]:
                dfs(nei, prev + adj[i][nei])
        
        dfs(k, 0)
        result = max(shortest)
        return result if result != float('inf') else -1