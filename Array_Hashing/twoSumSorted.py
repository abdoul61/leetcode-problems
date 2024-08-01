#Given a sorted array of interger find the pair adding to a target


from typing import List


class Solution:
    def __init__(self):
        pass

    def twoSumsorted(self,nums:List[int],target:int)->List[int]:
        l,r = 0,len(nums)-1
        while l < r:
            addval = nums[l] + nums[r]
            if addval == target:
                return [l+1,r+1]
            elif addval > target:
                r -= 1
            else:
                l += 1
        return []



numbers = [2,7,11,15]
target = 9
print(Solution().twoSumsorted(numbers,target))
            
