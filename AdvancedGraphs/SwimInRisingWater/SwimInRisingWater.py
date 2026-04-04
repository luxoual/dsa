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


