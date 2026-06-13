class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Top-down
        # Our basecase is when we are on a square that we
        # cant move from. At the minimum, we'll always have
        # at least 1 length at each tile
        # Instead of thinking about climbing, we can reverse it
        # and think about where can we go from this current tile
        # we can traverse to any tile that is < our current tile
        # and the longest strictly increasing path at this tile
        # is 1 + max(longestPath of neigbors)
        n = len(matrix)
        m = len(matrix[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cache = [[-1] * m for _ in range(n)]

        def traverse(x, y):
            if cache[x][y] != -1:
                return cache[x][y]

            # Haven't explored
            cache[x][y] = 1
            for nei in neighbors:
                dx = x + nei[0]
                dy = y + nei[1]
                if 0 <= dx < n and 0 <= dy < m and matrix[x][y] > matrix[dx][dy]:
                    # Valid neighbor
                    cache[x][y] = max(cache[x][y], 1 + traverse(dx, dy))

            return cache[x][y]

        result = 1
        for i in range(n):
            for j in range(m):
                result = max(result, traverse(i, j))
        return result
