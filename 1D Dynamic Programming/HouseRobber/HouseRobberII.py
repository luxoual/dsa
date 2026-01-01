class Solution:
    def rob(self, nums: List[int]) -> int:
        # Seems like essentially the same, except we can't use the first or last
        # 3 4 3 4 3
        # 2 9 8 3 6
        # 2 9 10 12 
        n = len(nums)
        if n <= 2:
            return max(nums[0], 0 if n != 2 else nums[1])

        first = [nums[0], max(nums[0], nums[1])]

        sec = [nums[1], max(nums[1], nums[2])]

        for i in range(2, n-1):
            temp1 = max(nums[i] + first[0], first[1])
            first[0] = first[1]
            first[1] = temp1

            j = i+1
            temp2 = max(nums[j] + sec[0], sec[1])
            sec[0] = sec[1]
            sec[1] = temp2
        
        return max(first[-1], sec[-1])

