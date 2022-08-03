# Leetcode problem called the 3Sum 

#here we need to return [num1,num2 , target] such that num1 + num2 = target
from typing import List

def fn(nums:List[int]) -> List[List[int]]:
    res = []
        # nlog(n) to sort the list
    nums.sort()
    for i , target , in enumerate(nums):
        if i > 0 and target == nums[i-1]:
            continue
        l = i + 1 
        r = len(nums) -1 
        while l < r:
            if target + nums[r] + nums[l] < 0:
                l += 1
            elif target + nums[r] + nums[l] > 0:
                r -= 1
            else:
                target + nums[r] + nums[l] == 0
                res.append([nums[l], nums[r], target])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res




print(fn([-1,0,1,2,-1,-4]))