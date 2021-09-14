class Solution:
    def reverse(self, x: int) -> int:

        negNum = False

        if x < 0:
            negNum = True
            x = -x
        revNum = 0

        while x:
            rem = x % 10
            revNum = revNum * 10 + rem
            x = x // 10

        if revNum >= 2 ** 31 -1 or revNum <= -2 ** 31:
            return 0
        return -revNum if negNum else revNum


a = Solution()
print(a.reverse(121))

