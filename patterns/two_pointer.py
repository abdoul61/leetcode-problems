

from typing import List

class Solution:
    def __init__(self):
        return None
    def twoPointer_sorted(self,nums:List[int],target:int)->List[int]:
        result = []
        left,right = 0,len(nums)-1
        while left <= right:
            val = nums[left] + nums[right]
            if val == target:
                return [left,right]
            elif val < target:
                left += 1
            else:
                right -= 1
        return result
    def twoPointer(self, nums:List[int],target:int)->List[int]:
        map = {}
        for el in range(len(nums)):
            val = target - nums[el]
            if val not in map:
                map[nums[el]] = el
            else:
                return [map[val],el]
        return [-1,-1]


s = Solution()
nums = [2, 7, 11, 15]
target = 9

print(s.twoPointer_sorted(nums,target))
print(s.twoPointer(nums,target))

