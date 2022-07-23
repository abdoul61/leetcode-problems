# This a problem called the Contains Duplicate


from typing import List


def fn(nums: List[int]) -> bool:
    seen ={}
    for num in nums:
        if num not in seen:
            seen[num] = 1
        else:
            return True
    return False  


l = [1,2,3,1]
b =  [1,2,3,1]
c = [1,2,3,4]
a = [1,1,1,3,3,4,3,2,4,2]
print(fn(l))
print(fn(a))
print(fn(b))
print(fn(c))