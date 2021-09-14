class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        number = x
        # Stoeing the x in number so that we can check it at the end of the code
        reverse = 0

        while number:
            #number = number % 10
            reverse = reverse * 10 + number % 10
            number = number // 10

        return x == reverse
