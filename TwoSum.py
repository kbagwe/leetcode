from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                elif nums[i] == target and nums[j] == target:
                    return [i, j]

    # Time Complexity is O(n)


class SolutionHash:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in result:
                return [i, result[diff]]
            result[num] = i
        return []

    # Time Complexity is 0(log(n))


class Solutionfast:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        sortedarray = sorted(zip(nums, range(len(nums))))
        while i < j:
            if sortedarray[i][0] + sortedarray[j][0] == target:
                return [sortedarray[i][1], sortedarray[j][1]]
            elif sortedarray[i][0] + sortedarray[j][0] < target:
                i += 1
            elif sortedarray[i][0] + sortedarray[j][0] > target:
                j -= 1






