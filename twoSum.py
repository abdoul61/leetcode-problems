#This is a leecode problem called two sum

from typing import List
def fn(nums: List[int],target:int)-> List[int]:
    seen = {}
    resul = []
    for i , num in enumerate(nums):
        #9-2 = 7
        #9-7 = 2
        res = target - num
        if res not in seen:
            seen[num]  = i
        else:
            resul.append(seen.get(res))
            resul.append(i)
    
    return resul




print(fn([2,7,11,15],9))
print(fn([3,2,4],6))
print(fn([3,3],6))
