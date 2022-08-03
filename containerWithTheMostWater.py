# Leetcode problem called the container with the most water


from typing import List


def fn(nums:List[int])-> int:
    maxWater = 0
    l , r = 0, len(nums)-1
    while l < r:
        water = (r-l)* min(nums[l],nums[r])
        maxWater = max(maxWater,water)
        if l < r:
            l += 1
        elif l > r:
            r -= 1
    return maxWater


print(fn( [1,8,6,2,5,4,8,3,7]))