#This problem is a leetcode problem called the search in rotated array

from typing import List

def search_cir(nums:List[int],target:int)->int:
    l,r = 0,len(nums)-1

    while l <= r:
        m = (l + r)//2
        if target == nums[m]:
            return m
        if nums[l] <= nums[m]:
            # left side [4,5,6,7,8,9,0,1,2,3] 
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r  = m -1
        else:
            if target <  nums[m] or  target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1


print(search_cir([4,5,6,7,8,9,0,1,2,3],0))






