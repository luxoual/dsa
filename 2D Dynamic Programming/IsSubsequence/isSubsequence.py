class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # "" is always a subsequence of anything
        # thats our basecase
        n = len(s)
        m = len(t)

        cache = [[-1] * m for _ in range(n)]

        def dp(i, j):
            if n == i:
                return True

            if m == j:
                return False

            if cache[i][j] != -1:
                return cache[i][j]

            # Traversal
            cache[i][j] = False
            if s[i] == t[j]:
                cache[i][j] = cache[i][j] or dp(i + 1, j + 1)
            else:
                cache[i][j] = cache[i][j] or dp(i, j + 1)

            return cache[i][j]

        return dp(0, 0)
