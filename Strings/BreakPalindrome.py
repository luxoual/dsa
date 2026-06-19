class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2:
            return ""

        # A few different cases
        # we ideally want to change the first letter we can
        # to the letter "a", unless we run into a situation
        # where turning it into an a would not help us,
        # which would be when the first half of the palindrome
        # is all 'a's, thats when we turn the first letter
        # to a 'b'.
        for i in range(n // 2):
            if palindrome[i] != "a":
                return palindrome[0:i] + "a" + palindrome[i + 1 :]

        return palindrome[0 : n - 1] + "b"
