#problem statement: given a non negative interger representing an elevation map 
# where each bar is 1, computer how much water it can trap.


from typing import List
class Solution:
    def __init__(self):
        pass
    def trappingwater(self,heights:List[int])->int:
        l,r = 0,len(heights)-1
        maxLeft,maxRight = heights[l],heights[r]
        result = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft,heights[l])
                result += maxLeft - heights[l]
            else:
                r -= 1
                maxRight = max(maxRight,heights[r])
                result += maxRight - heights[r]
        return result

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trappingwater(height))
