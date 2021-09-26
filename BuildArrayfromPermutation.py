from typing import List

class Solution:
        def buildArray(self, nums: List[int]) -> List[int]:
            ans = []
            for i in range(0, len(nums)):
                print((nums[nums[i]]))
                ans.append(nums[nums[i]])
            return ans

