class Solution:
    def rob(self, nums: List[int]) -> int:
        # Lets try thinking of the bruteforce recurison
        # What if we considered, whats the most amount of money
        # we can rob at this very point
        # The base cases would be nums[0] and nums[1]
        # 4 1 2 3
        # 4 1 6
        # 4 4 6 3
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        i = 2
        tab = [nums[i-2], nums[i-1]]
        while i < n:
            temp = max(tab[0] + nums[i], tab[1])
            tab[0] = max(tab[0], tab[1])
            tab[1] = temp
            i+=1
        
        return tab[1]
            

            


    