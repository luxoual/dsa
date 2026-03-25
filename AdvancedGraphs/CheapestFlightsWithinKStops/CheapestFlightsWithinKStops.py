# Bruteforce DFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # We are looking for the shortest path
        # to dst from src, 
        adj = defaultdict(list)
        for flight in flights:
            # Price and dst
            adj[flight[0]].append((flight[2], flight[1]))

        # DFS Bruteforce
        # We can try all the paths, keep track of
        # how many flights we've taken so far
        # if we taken too many, then we return float('inf')
        # if we reach the dst, we return our total so far
        visited = set([src])
        def dfs(total, taken, curr):
            print(curr)
            print(taken)
            nonlocal dst
            if curr == dst:
                return total
            if taken > k:
                return float('inf')
            
            # Traverse
            result = float('inf')
            for cost, dest in adj[curr]:
                if dest not in visited:
                    visited.add(dest)
                    result = min(result, dfs(total + cost, taken+1, dest))
                    visited.remove(dest)

            return result
        cheapest = dfs(0, 0, src)
        return -1 if cheapest == float('inf') else cheapest

# Dijkstra's Algorithm (without visited, keeping track of stops because we have to address all the ways to get to a node)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # We are looking for the shortest path
        # to dst from src, 
        adj = defaultdict(list)
        for flight in flights:
            # Price and dst
            adj[flight[0]].append((flight[2], flight[1]))

        # Dijkstras
        heap = []
        # Distances to reach [node] in [flights] dist[node][flights] = dist
        distances = [[float('inf')] * (k+2) for _ in range(n)]
        distances[src][0] = 0
        # Cost, Dest, Stops
        heapq.heappush(heap, (0, src, 0))
        while heap:
            cost, dest, stops = heapq.heappop(heap)
            if dest == dst: return cost
            # If we haven't reached
            if stops > k: continue
            for nei in adj[dest]:
                newDst = cost + nei[0]
                # Prune any distances that are worse
                # than what we already have
                if distances[nei[1]][stops+1] > newDst:
                    distances[nei[1]][stops+1] = newDst
                    heapq.heappush(heap, (newDst, nei[1], stops + 1))
        return -1

# Bellman-Ford Algorithm (not most optimized but is simple to understand)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # The finalized prices, at this current level/layer
        # of our traversal
        prices = [float('inf')] * n
        prices[src] = 0
        
        for i in range(k + 1):
            # Go through every single edge
            temp = prices[::] # Copy
            for s, d, p in flights:
                price = prices[s] + p
                if price < temp[d]:
                    temp[d] = price
            prices = temp
        
        return prices[dst] if prices[dst] != float('inf') else -1




