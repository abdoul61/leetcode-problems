



from typing import List



class Solution:
    def __init__(self):
        pass

    def function(self,heights:List[int])->int:
        maxArea = 0
        stack = []

        for i, hei in enumerate(heights):
            start = i
            while stack and stack[-1][1] > hei:
                index,height = stack.pop()
                maxArea = max(maxArea,(i-index) * height)
                start = index
            stack.append((start,hei))

        for i,h in stack:
            maxArea = max(maxArea,(len(heights)-i) * h)

        return maxArea


s = Solution()
print(s.function([2,1,5,6,2,3]))

