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
    
# Bellman-Ford Algorithm (optimized, using a queue to save time on traversing all edges + copying arrays)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford's Algorithm for finding the 
        # shortest path in max k stops

        # Involves layer by layer traversal (sorta like BFS)
        # Where the number of layers we traverse in this case
        # will be k+1, and at each layer traversal, we go
        # through all of the edges we have

        # We keep track of 2 arrays:
        # a distances array
        # which keeps track of the shortest distances to each
        # point, at this current level
        # and a temporary array
        # which is a copy of the distances array that gets modified
        # during the traversal, and at the end, we sync the
        # temporary array to the distances array

        # Adjacency List
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[2], flight[1]))
        
        # Starting off with one point
        distances = [float('inf')] * n
        distances[src] = 0

        q = deque([(0, src, 0)])
        while q:
            c, curr, stops = q.popleft()
            
            for cost, nei in adj[curr]:
                # The cost coming from start on this edge
                price = c + cost
                # If its cheaper than our current distance
                # replace it in our temp
                if price < distances[nei] and stops <= k:
                    distances[nei] = price
                    q.append((price, nei, stops + 1))
            # replace at the end because distances
            # holds our distances at that level, and
            # we need that until we go through all edges
        
        return distances[dst] if distances[dst] != float('inf') else -1






