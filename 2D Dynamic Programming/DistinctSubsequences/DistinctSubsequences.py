class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # What are my basecases
        # reaching the end of s and reaching the end of t
        # if i'm at the end of t, then that means i made
        # a subsequence, but if i make it to the end of s
        # but didn't make it to the end of t, then i didnt
        # create a subsequence

        # whenever i find a letter at s[i] == t[j]
        # i can choose to take the letter, or skip it
        # at each index, the number of subsequences i can
        # make at this index, is the number of subsequences
        # i can make of t[j+1] if i take the letter and
        # the number of subsequences of t[j] if i skip this letter

        n = len(s)
        m = len(t)

        if m > n:
            return 0

        # For times where we repeat
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if j == m:  # if i reach end of t first
                return 1  # I made a subsequence

            if i == n:  # if i reach end of s first
                return 0  # I didn't finish a subsequence

            if cache[i][j] != -1:
                return cache[i][j]

            # Go through the backtracking
            cache[i][j] = 0
            if s[i] == t[j]:  # Take the letter
                cache[i][j] += dfs(i + 1, j + 1)
            # we always have the option to skip
            cache[i][j] += dfs(i + 1, j)

            return cache[i][j]

        return dfs(0, 0)
