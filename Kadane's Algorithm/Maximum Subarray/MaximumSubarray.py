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

# Feb 18th redo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # If the curr subarray that we've seen so far, is
        # less than the curr number we could add, then we 
        # restart the subarray, we keep track of a running max

        # EDIT: The actual "state", that indicates that its not
        # worth keeping, is when keeping it absolutely can't 
        # assist teh most optimal solution, where in this case
        # if any curr subarray sum, is negative, then we should
        # replace it, not just when the curr subarray sum is less
        # than the curr number.

        result = nums[0]
        n = len(nums)
        curr = nums[0]
        for start in range(1,n):
            if curr <= 0:
                # Not worth keeping
                curr = nums[start]
            else:
                curr += nums[start]
            result = max(result, curr)
        
        return result

