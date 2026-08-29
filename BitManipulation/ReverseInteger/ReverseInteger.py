class Solution:
    def reverse(self, x: int) -> int:
        # Then lets, set some boundaries as in the
        # max and min 32 bit integers we can have

        MAX = 0x7FFFFFFF  # Max positive 2147483647
        MIN = -0x80000000  # Minimum negative -2147483648

        # Check for if its negative to begin with
        negative = True if x < 0 else False

        result = 0
        while x != 0:
            digit = abs(x) % 10
            x = abs(x) // 10
            if negative:
                x = x * -1
                digit = digit * -1

            if result > MAX // 10 or result < -(abs(MIN) // 10):
                # No matter what digit you add itll overflow
                return 0
            if result == MAX // 10 and digit > 7:
                return 0
            if result == MIN // 10 and digit < -8:
                return 0
            result *= 10
            result += digit

        return result
