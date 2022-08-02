# Leetcode problem called the two Sum II 

from typing import List

def fn(nums: List[int],target:int) -> List[int]:
    l = 0
    r = len(nums) - 1
    while l < r:
        valid = nums[l] + nums[r]
        if valid == target:
            return [l+1,r+1]
        elif valid > target:
            r = r-1
        elif valid < target:
            l = l + 1
    return []



print(fn([2,7,11,15],9))