class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minProduct = nums[0] 
        res = nums[0]

        for i in range(1,len(nums)):
            tmp = nums[i] * maxProduct
            maxProduct = max(tmp, nums[i] * minProduct, nums[i])
            minProduct = min(tmp, nums[i] * minProduct, nums[i])
            res = max(res, maxProduct)

        return res
