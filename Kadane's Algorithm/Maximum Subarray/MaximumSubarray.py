# Solution considering negative directly
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Notice that we have a choice at each index, to either
        # take the current number (to continue) or we can restart
        # at each index, it represents the best subarray sum,
        # at this length of the subarray.
    
        result = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            if curr < 0: # We know that negative is not going to help, so we can just reset it to this.
                curr = 0
            curr += nums[i]
            result = max(curr, result)

        return result
    
# Solution without resetting the curr to zero
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Notice that we have a choice at each index, to either
        # take the current number (to continue) or we can restart
        # at each index, it represents the best subarray sum,
        # at this length of the subarray.
    
        result = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            curr += max(curr + nums[i], nums[i])
            result = max(curr, result)

        return result

