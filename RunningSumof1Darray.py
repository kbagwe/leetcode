from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
            ans = [0] * len(nums)
            ans[0] = nums[0]
            for i in range(1, len(nums)):
                print(ans[i], ans[i-1], nums[i])
                ans[i] = ans[i - 1] + nums[i]
            return ans

