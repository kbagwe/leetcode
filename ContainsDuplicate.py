from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()
    #Using hashmap
        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True

        return False


