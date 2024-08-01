# You are given a list of heights of multiple position 
# of a water container.
# find the largest container.




from typing import List


class Solution:
    def __init__(self):
        pass
    def containerWith(self,heights:List[int])->int:
        maxArea = 0
        l,r = 0,len(heights)-1
        while l < r:
            area = (min(heights[l],heights[r])) * (r-l)
            maxArea = max(maxArea,area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea



height = [1,8,6,2,5,4,8,3,7]
print(Solution().containerWith(height))
