class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = 0

        for i in range(len(t)):
            if m == n:
                return True
            if t[i] == s[m]:
                m += 1

        return True if m == n else False
