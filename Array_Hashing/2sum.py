# Problem statment: find the index of two interger if they add 
# to the target given.


from typing import List
class Solution:

    def __init__(self):
        pass
    def twoSum(self,nums:List[int],target:int)->List[int]:
        map = {}
        for i,el in enumerate(nums):
            complement = target - el
            if complement in map:
                return [i,map[complement]]
            else:
                map[el] = i
        return []

s = Solution()
print(s.twoSum([2,7,11,15],9))

