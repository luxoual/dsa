class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # We traverse through the length of word2,
        # whenever we have a differing letter between
        # word1 and word2, we consider our possible operations
        # We end when we finish traversing all of word2 and
        # n == m? For the case of when word1 is longer

        n = len(word1)
        m = len(word2)

        cache = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            # i is the index in word1
            # j is the index in word2
            if i == n:
                # We reached the end of word1 first
                # so we need to add whats left of the
                # other word
                return m - j

            if j == m:
                # Same thing but other way around
                return n - i

            if cache[i][j] != -1:
                return cache[i][j]

            result = float("inf")
            if word1[i] != word2[j]:
                # Try all operations

                # If delete from word1, then we can move it up 1
                result = min(result, dfs(i + 1, j))

                # If we add to word1, then we can move word2 up 1
                result = min(result, dfs(i, j + 1))

                # If we replace, then we move both
                result = min(result, dfs(i + 1, j + 1))

                result += 1
            else:
                result = dfs(i + 1, j + 1)

            cache[i][j] = result
            return result

        return dfs(0, 0)
