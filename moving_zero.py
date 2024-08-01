from typing import List


class Solution:
    def __init__(self):
        return None


    def func(self,nums:List[int])->List[int]:
        def swap(a,b,nums):
            nums[a],nums[b] = nums[b],nums[a]
        for i in range(len(nums)):
            if nums[i] == 0 and nums[-1] != 0:
                swap(i,-1,nums)
            if nums[i] == 0:
                el = nums.pop(i)
                nums.append(el)
        return nums
    def func2(self,nums:List[int])->List[int]:
        idx = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > 0:
                nums[idx],nums[i] = nums[i],nums[idx]
                idx -= 1

        return nums[::-1]



nums = [1,0,4,6,0,7,9,0,0,13]

print(Solution().func(nums))
print(Solution().func2(nums))
