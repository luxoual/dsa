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
