# DFS Backtracking
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Backtracking DFS, at each cell we can try all 4 directions
        # What we want is the minimum amount of water that we
        # need to reach the end, where on one path, that number
        # is the highest elevation we have in that path.
        # So at each cell, we are saying what is the minimum elevation
        # of the 4 directions that we can go, that we can reach
        # the end.
        n = len(grid)
        visited = set() # For cycles in backtracking
    
        def dfs(x, y, water):
            if x == n-1 and y == n-1:
                return water
            
            # Traversal
            visited.add((x,y))
            lowest = float('inf')

            for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                if 0 <= dx + x < n and 0 <= dy + y < n and (dx + x, dy + y) not in visited: # Not on this path
                    next_water = max(water, grid[dx+x][dy+y])
                    lowest = min(lowest, dfs(dx+x, dy+y, next_water))
            
            visited.remove((x,y)) # Remove from the path
            return lowest

        return dfs(0, 0, grid[0][0])

# Dijkstra's Algorithm
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Attempting Dijkstras attempt
        # visited set with (x,y) coordinates
        # heap with (water, x, y)
        # whenever we pop from the heap, its the least
        # amount of water to reach this cell
        # so we add it to visited
        # We traverse through the directions, using
        # max(water, grid[nx][ny]), if we find any
        # visited cells, then we just skip this one,
        # the first time we pop from the heap with
        # the bottom right cell, we just return
        visited = set()
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        directions = [(0,1), (-1,0), (1,0), (0,-1)]
        while heap:
            water, x, y = heapq.heappop(heap)
            if x == n-1 and y == n-1: return water
            if (x,y) in visited: continue
            visited.add((x,y))

            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                    heapq.heappush(heap, (max(water, grid[nx][ny]), nx, ny))





