#The sliding window patterns 
# When ? if the data structure involve is linear(array, string)
# they are asking to find the longuest, shortest , average 
# the brute force is most likely 0(n^2)
from typing import List

class Solution:
    def __init__(self):
        return None
    
    def slidingWindow(self,nums:List[int],k:int)->float:
        start = 0
        _sum = 0
        average = []
        for end in range(len(nums)):
            _sum += nums[end]

            if end >= k - 1:
                val = _sum / 4
                average.append(val)
                _sum -= nums[start]
                start += 1
        return max(average)



s = Solution()
k = 4
nums = [1, 12, -5, -6, 50, 3]
print(s.slidingWindow(nums,k))
