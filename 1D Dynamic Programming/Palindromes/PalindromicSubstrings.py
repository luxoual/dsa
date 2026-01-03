# Two Pointer
class Solution:
    def countSubstrings(self, s: str) -> int:
        # The bruteforce would be to just go through
        # each and every substring and check if its
        # a palindrome which would be n^3

        # But we can make use of what we learned previously
        # with two pointers and dp, on how this substring
        # is a palindrome if s[l] == s[r] and s[l+1 : r] is a
        # a palindrome

        # Two Pointers - Whenever we find a non-palindrome
        # we can skip to the next letter
        # 2 Loops, handling odd and even case
        result = 0
        n = len(s)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                result+=1
                l-=1
                r+=1

            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                result+=1
                l-=1
                r+=1
        
        return result

# DP Solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        # The bruteforce would be to just go through
        # each and every substring and check if its
        # a palindrome which would be n^3

        # But we can make use of what we learned previously
        # with two pointers and dp, on how this substring
        # is a palindrome if s[l] == s[r] and s[l+1 : r] is a
        # a palindrome

        # Dp Solution -> Our base cases are sizes 1-3
        # Size 1 : Always a palindrome
        # Size 2 : We only care if s[l] == s[r]
        # Size 3 : We only care if s[l] == s[r] b/c the "inside"
        # is always a palindrome

        # So we need to keep track of already checked substrings, so
        # we don't need to recheck if the inside is a palindrome
        result = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j + 1 <= 3 or dp[j+1][i-1]):
                    dp[j][i] = True
                    result+=1
        
        return result


            