class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = x
        product = 0

        while x > 0:
            digit = x % 10
            product = product * 10 + digit
            x = x // 10

        return product == y