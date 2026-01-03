# Top Down
class Solution:
    def numDecodings(self, s: str) -> int:
        # Some possible base cases -> Every single digit
        # maps to some character

        # If we ever see a 0, then we need a digit before,
        # or else it doesnt work -> Base case 
        # Decoding involves decoding the entire thing
        n = len(s)
        cache = [-1] * n # cache[i] = number of ways to decode s[i::]

        def dp(i): # Number of ways to decode
            nonlocal n
            if i >= n:
                return 1
            
            if cache[i] != -1: 
                return cache[i]
            
            if s[i] == "0":
                return 0

            if i == n-1:
                return 1
            
            cache[i] = dp(i+1) # You can always take the current if its not a 0

            if i + 1 < n and int(s[i:i+2]) <= 26:
                cache[i] += dp(i+2)
            
            return cache[i]
        
        return dp(0)

            
        
            
        