# Bruteforce
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Bruteforce is try all possible subarrays, and find
        # the max sum of them. Only make subarrays of n size.

        n = len(nums)
        result = nums[0]
        for i in range(n):
            curr = 0
            for j in range(n):
                curr += nums[(i + j - 1) % n]
                result = max(result, curr)
        
        return result

# Use Kadane's Algorithm (instead of maxEndingHere, we also use minEndingHere)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # So if the subarray is either a regular subarray
        # or a circular one
        # we can check for a linear one first with
        # the old solution and then we can check for a
        # wrapped one, but only difference is that
        # we are looking for the minimum/negative subarray
        # in the middle

        result = float('-inf')
        curr = 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            result = max(result, curr)
        
        curr = 0
        mini = float('inf')
        for num in nums:
            if curr > 0:
                curr = 0
            curr += num
            mini = min(mini, curr)
        
        whole = sum(nums)
        result = max(result, whole - mini if whole != mini else result)

        return result



