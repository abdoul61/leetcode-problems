# Problem statment: find the index of three interger if they add 
# to the target given.


#Solution: sort the array and use the two pointer to find the pair(i,j)
#make sur not include duplicate at the beginning and when finding the pai

from typing import List
class Solution:

    def __init__(self):
        pass
    def threeSum(self,nums:List[int])->List[int]:
        result = []
        nums.sort()
        for i,el in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l < r:
                target = nums[l] + el + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    result.append([el,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return list(result)

s = Solution()
# print(s.twoSum([2,7,11,15],9))
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))

