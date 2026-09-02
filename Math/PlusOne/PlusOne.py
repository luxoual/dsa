class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        result = [0] * (n + 1)
        result[-1] = 1

        for i in range(n - 1, -1, -1):
            digit = digits[i] + result[i + 1]
            if digit == 10:
                result[i] += 1
            result[i + 1] = digit % 10

        if result[0] != 0:
            return result
        return result[1::]
