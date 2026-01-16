class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # So in this case, the maximum product of a subarray
        # in this array, is the same as hte maximum subarray
        # of everything in nums, not including the last number
        
        # in this case, we have to think about how we can get
        # a max product, where we consider negatives
        # negatives can turn our originally lowest product
        # into our greatest one

        # notice that, we always have to change hte currMax or currMin
        # it can't just keep what it was before includign this number
        # or essentially currMax can't be currMax after getting to a #
        # because its either we include hte previous or we start here

        result = nums[0]
        currMax, currMin = nums[0], nums[0]

        for i in range(1, len(nums)):
            # if nums[i] is positive, then nums[i] * currMax will help
            # if nums[i] is negative, then nums[i] * currMin will help
            # sometimes the prefix doesnt help like (2, -1)
            oldMax = currMax
            currMax = max(nums[i] * currMax, nums[i] * currMin, nums[i])

            # Same thing as the currMax, except negatives * currMax can help
            # and postives * currMin can help.
            # BOTH r possibilities because the currMax could be negative or postiive
            # so can currMin (be negative or positive)
            currMin = min(nums[i] * oldMax, nums[i] * currMin, nums[i])
            result = max(result, currMax)
        
        return result

