# Leetcode problem called trapping rain water 



from turtle import right
from typing import List

def fn(nums:List[int])-> int:
    left = 0
    rigth = len(nums)-1
    max_left = nums[left]
    max_rigth = nums[rigth]

    trapped = 0

    while left < rigth:
        if nums[left] < nums[rigth]:
            if max_left < nums[left]:
                max_left = nums[left]
            else:
                trapped += max_left - nums[left]
            left += 1
        else:
            if max_rigth < nums[rigth]:
                max_rigth = nums[rigth]
            else:
                trapped += max_rigth - nums[rigth] 
            rigth -= 1
    return trapped



print(fn([0,1,0,2,1,0,1,3,2,1,2,1]))
print(fn([4,2,0,3,2,5]))

