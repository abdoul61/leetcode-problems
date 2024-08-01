# Given an array of integers temperatures represents the 
# daily temperatures, return an array answer such that 
# answer[i] is the number of days you have to 
# wait after the ith day to get a warmer temperature. If 
# there is no future day for which this i
# s possible, keep answer[i] == 0 instead.

from typing import List

class Solution:
    def __init__(self):
        pass

    def function(self,temperatures:List[int])->List[int]:
        re = [0] * len(temperatures)
        stack = [] # track [el,idx]
        for i,elem in enumerate(temperatures):
            while stack and stack[-1][0] < elem:
                el,idx = stack.pop()
                re[idx] = (i - idx)
            stack.append([elem,i])
        return re
    


s = Solution()
print(s.function([73,74,75,71,69,72,76,73]))
