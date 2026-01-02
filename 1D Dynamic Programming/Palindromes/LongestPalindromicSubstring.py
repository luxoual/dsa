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


