# Original / First attempt at Top-down

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Base Case is the string is in wordDict or empty
        # We can't traverse a path, if none of the
        # current string is in wordDict

        cache = {} # If its in cache, we've seen it before
        # dfs(s) will return True if s can be segmented

        def dfs(s):
            if s in wordDict or not s:
                return True
            
            if s in cache:
                return cache[s]
            
            # Traversal
            for i in range(len(s)):
                curr = s[:i+1]
                leftover = s[i+1::]
                if curr in wordDict and dfs(leftover):
                    cache[s] = True
                    return True
            
            cache[s] = False
            return False
        
        return dfs(s)

# Optimized Top-down
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Base Case is the string is in wordDict
        # We can't traverse a path, if none of the
        # current string is in wordDict

        # dfs(i), can the current string be broken into segments
        # s[i::]
        n = len(s)
        cache = {}
        one = set(wordDict)

        def dfs(i):
            if i == n:
                return True
            
            if i in cache:
                return cache[i]
            
            # Traversal
            for j in range(i, n):
                curr = s[i:j+1]
                if curr in one and dfs(j+1):
                    cache[i] = True
                    return True
            
            cache[i] = False
            return False
        
        return dfs(0)
                

                
# Bottom-up
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        one = set(wordDict)
        dp = [False] * (n+1)
        dp[n] = True # Empty string is true

        for i in range(n-1, -1, -1):
            for word in wordDict:
                m = len(word)
                if i + m <= n and s[i:i + m] in one and dp[i+m]:
                    dp[i] = True
                    break
            
        return dp[0]


