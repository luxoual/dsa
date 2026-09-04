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


# Second Run at it
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        results = digits.copy()
        for i in range(len(digits) - 1, -1, -1):
            result = carry + digits[i]
            results[i] = result % 10
            if result < 10:
                return results
        return results if not carry else [1] + results
