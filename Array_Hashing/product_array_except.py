# The problem statment is to compute the product of each 
# all elements at position i except that element



from typing import List

class Solution:
    def __init__(self):
        pass

    def productExcept(self,nums:List[int])->List[int]:
        res = [1] * len(nums)

        prefix,suffix = 1,1
        # computer from the left to the right
        for i in range(len(nums)):
            res[i] = prefix 
            prefix  *= nums[i]

        # computer from right to left

        for i in range(len(nums)-1,-1,-1):
            res[i] = suffix * res[i]
            suffix = nums[i] * suffix
        return res 


print(Solution().productExcept([1,2,3,4]))
        
