# Bruteforce
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # At eahc level of nums, we need to loop through
        # each number, and try popping that balloon,

        def popBalloon(arr):
            length = len(arr)
            result = 0
            for i in range(length):
                value = arr[i]
                if i >= 1:
                    value *= arr[i - 1]
                if i < length - 1:
                    value *= arr[i + 1]
                result = max(result, value + popBalloon(arr[:i] + arr[i + 1 :]))
            return result

        return popBalloon(nums)


# Topdown DP
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Instead of going through every option, and then
        # modifying the array, we want to save the array
        # creation and modification

        # So we can think about it backwards, we can start
        # with which balloon are we going to pop last

        # the very last balloon, is multiplied by the very last
        # balloon of the subarray on the left side and the very
        # last balloon of the subarray on the right side
        # Which is why nums[l-1] * nums[i] * nums[r+1]
        # The last balloon becomes the right side of the left subarray
        # the left side of the right subarray (b/c the last balloon would
        # multiply by that & the bordering value of 1)

        # Instead of keeping track of these subarrays, we can
        # use indexes l, r which maps the bounds of these subarrays

        length = len(nums)
        nums = [1] + nums + [1]
        cache = [[-1] * (length + 2) for _ in range(length + 2)]

        def popBalloon(l, r):
            if l > r:
                return 0

            if cache[l][r] != -1:
                return cache[l][r]

            cache[l][r] = 0

            for i in range(l, r + 1):
                value = nums[l - 1] * nums[i] * nums[r + 1]
                cache[l][r] = max(
                    cache[l][r], value + popBalloon(l, i - 1) + popBalloon(i + 1, r)
                )

            return cache[l][r]

        return popBalloon(1, length)
