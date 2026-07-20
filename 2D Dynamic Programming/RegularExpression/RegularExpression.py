class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # We can go along p, and keep going unless
        # something doesn't match, so we can just
        # return from there

        # if we are dealing with a *, we only need to
        # move p, if the current letter in s, doesn't
        # match what is p[j - 1]

        # if we reach the end of s we return true
        # else if we reach the end of p first we return false?

        n = len(s)
        m = len(p)

        cache = [[None] * (m + 2) for _ in range(n + 2)]

        def dp(i, j):
            # i index for s
            # j index for p
            if i == n and j == m:
                return True

            if j == m and i != n:
                return False

            if cache[i][j] is not None:
                return cache[i][j]

            cache[i][j] = False
            if i < n and (s[i] == p[j] or p[j] == "."):
                # Then we can move forward in s[i]
                if j < m - 1 and p[j + 1] == "*":
                    # 2 Options, we stay where we are
                    # or we can skip both
                    cache[i][j] = cache[i][j] or dp(i + 1, j)
                cache[i][j] = cache[i][j] or dp(i + 1, j + 1)
            if j < m - 1 and p[j + 1] == "*":
                cache[i][j] = cache[i][j] or dp(i, j + 2)

            return cache[i][j]

        return dp(0, 0)
