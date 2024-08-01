from typing import List


class Solution:
    def __init__(self):
        return None
    def func(self,nums:List[int])->int:
        cost = 0
        for b in nums:
            if cost % 2 == 0:
                b = b
            else:
                b = not b
            if b % 2 == 1:
                continue
            else:
                cost += 1
        return cost

nums = [1,0,1,1,0,0,1]
print(Solution().func(nums))
