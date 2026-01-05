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

# Bottom Up
class Solution:
    def numDecodings(self, s: str) -> int:
        # Let's try bottom-up, where we now start with our
        # base cases: a single number is always decodable
        # as long as its not a 0

        # Number of ways to decode is the number of ways to
        # decode dp(i+1) + dp(i+2) if the pair is valid
        # when theres nothing left, then its just 1
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i+2 <= n and int(s[i:i+2]) < 27:
                    dp[i] += dp[i+2]
        
        return dp[0]

# Bottom Up - Space Optimized
class Solution:
    def numDecodings(self, s: str) -> int:
        # Let's try bottom-up, where we now start with our
        # base cases: a single number is always decodable
        # as long as its not a 0

        # Number of ways to decode is the number of ways to
        # decode dp(i+1) + dp(i+2) if the pair is valid
        # when theres nothing left, then its just 1
        n = len(s)
        curr = 0
        curr1 = 1
        curr2 = 0
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = curr1
                if i+2 <= n and int(s[i:i+2]) < 27:
                    curr += curr2
            
            curr, curr1, curr2 = 0, curr, curr1
        
        return curr1


            
        
            
        