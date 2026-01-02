# Two Pointer
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # The Bruteforce doesn't really give us any subproblems
        # that we can work with to reuse some information
        # If dive into what we are used to with Palindromes
        # We check if something is a palindrome using two-pointers
        # and a easy base case is a single letter.
        # Now if we go from lets say the middle character,
        # and expand outwards, we could eventually find 
        # a string that isn't a palindrome
        # abaad -> wouldn't work
        # Now what if you continue beyond just starting at the middle
        # We follow the same strategy, but at each index
        # but we can't just only have a basecase of 1 letter, bc 1 + even,
        # will always be odd, so we need to check pairs of 2 letters
        # so we can handle even number palindromes
        
        result = ""
        length = 0
        n = len(s)
        # Odd
        for i in range(n):
            # Expand outward by 2
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > length:
                    result = s[l:r+1]
                    length = r - l + 1
                l-=1
                r+=1
        # Even
            # Expand outward by 2
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > length:
                    result = s[l:r+1]
                    length = r - l + 1
                l-=1
                r+=1

        return result

# DP Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStart = 0
        length = 0
        n = len(s)
        
        # Represents substrings that are palindromes or not
        # for example - dababad
        # if we know 'bab' is a palindrome (i = 2, j = 4)
        # then if i=1, j=5, are the same letter, then 
        # ababa is a palindrome
        dp = [[False] * n for _ in range(n)]

        # We start from the right because we need to know
        # dp[i+1][j-1] before we can solve dp[i][j]
        # Inside is solved before the outside
        for i in range(n-1,-1,-1): 
            for j in range(i,n):
                # If the end letters match, and either its a basecase
                # 1 letter -> always palindrome
                # 2 letter -> only i and j need to match
                # 3 letter -> we only need to check i and j again
                # or the inside is a palindrome
                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > length:
                        resStart = i
                        length = j - i + 1
                    
        return s[resStart: resStart + length]


