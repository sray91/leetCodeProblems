#this is my first leetCode attempt
class Solution:
    def twoSum(self, integers: List[int], target: int) -> List[int]:
        passed = {}
        for i, num in enumerate(integers):
            # check if the complement to target of integers[i], had already been in integers
            if target - num in passed:
                return [i, passed[target - num]]
            else:
                passed[num] = i
