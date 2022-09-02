from typing import List
def binary_search(nums:List[int],target:int)->int:
    l,r = 0, len(nums)-1

    while l <= r:
        m = (l+r)// 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

lst = [9,12,45,55,64,78]
print(binary_search(lst,9))

