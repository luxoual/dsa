class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Full Adder
        # 0 1
        # 1 1
        carry = 0
        result = 0
        cutoff = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        a &= cutoff
        b &= cutoff

        for i in range(32):
            mask = 1 << i
            sum_bit = (a & mask) ^ (b & mask) ^ (carry)
            result |= sum_bit
            carry = 2 * mask if ((a & mask) + (b & mask) + carry) >= 2 * mask else 0

        if result > max_int:  # This number is actually negative
            result -= 2**32

        return result
