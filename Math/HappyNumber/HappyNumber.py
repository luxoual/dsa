class Solution:
    def isHappy(self, n: int) -> bool:
        # All multiples of 10 are non-cylical numbers
        # We can stop if we reach the same number again
        found = set()

        # Squares
        def sumSquare(number):
            result = 0
            while number != 0:
                digit = number % 10
                number = number // 10
                result += digit**2
            return result

        while True:
            if n == 1:
                return True

            else:
                n = sumSquare(n)
                if n in found:
                    return False  # Cycle
                found.add(n)


class Solution:
    def isHappy(self, n: int) -> bool:
        # All multiples of 10 are non-cylical numbers
        # We can stop if we reach the same number again

        # Squares
        def sumSquare(number):
            result = 0
            while number != 0:
                digit = number % 10
                number = number // 10
                result += digit**2
            return result

        slow = sumSquare(n)
        fast = sumSquare(slow)

        while True:
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
            fast = sumSquare(sumSquare(fast))
            slow = sumSquare(slow)
