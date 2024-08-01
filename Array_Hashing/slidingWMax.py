
#Problem statment: You given a list of number and are ask to slide a window of size k from the very to the right  side 
# of the array. you can only see k number at a time. return the max sliding window

# How to solve it: The principle is to use the monotone decreasing quee.
# 
from typing import List
import collections


class Solution:
    def __init__(self):
        pass
    def slidingW(self,nums:List[int],k:int)->List[int]:
        if len(nums) < k:
            return nums
        que = collections.deque() # this will take only the index of the nums
        # window = nums[0:k]
        # print(window)
        result = []
        l,r = 0,0
        while r < len(nums):
            while que and nums[r] > nums[que[-1]]:
                que.pop()
            que.append(r)

    #edge case: in case the left pointer is out bound then pop from the left
            if l > que[0]:
                que.popleft

            if (r-l+1) >= k:
                result.append(nums[que[0]])
                l += 1
            r += 1

        return result


print(Solution().slidingW([1,3,-1,-3,5,3,6,7],3))





