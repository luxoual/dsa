class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        q = deque([0]) # Starting at 0
        # shortest path to amount, via coins
        # coins are neighbors
        seen = set([0]) # amounts we already been to
        # we don't need to recheck anything because if
        # we got there earlier, we got there in less coins
        level = 0

        while q:
            for i in range(len(q)):
                curr = q.popleft() 
                if curr == amount: # Stop
                    return level
                
                # Traverse
                for coin in coins:
                    if curr + coin not in seen and curr + coin <= amount:
                        q.append(curr + coin)
                        seen.add(curr+coin)
            level+=1
        
        return -1


        

                    


        



        