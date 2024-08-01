# __import__('ipdb').set_trace(context=21)
from typing import List

class Solution:
    def __init__(self):
        pass
    def containsDuplicate(self,nums:List[int])->bool:
        # return len(set(nums)) != len(nums)
        my_set = set() 
        for i, el in enumerate(nums):
            if el in my_set:
                return True
            else:
                my_set.add(el)
        return False


nums1 = [1,1,1,3,3,4,3,2,4,2]
nums2 = [1,2,3,4,5]
nums3 = [1,2,3,4,1]
nums4 = [3,3]
s = Solution()
print(s.containsDuplicate(nums1))
print(s.containsDuplicate(nums2))
print(s.containsDuplicate(nums3))
print(s.containsDuplicate(nums4))
