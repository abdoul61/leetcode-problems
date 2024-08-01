from typing import List


class Solution:
    def __init__(self):
        return None

    def func(self,s:str,k:int)->str:
        result = ""
        stack = [] # [count,ch]
        for c in s:
            if stack and stack[-1][1] == c:
                stack[-1][0] += 1
            else:
                stack.append([1,c])
            if stack[-1][0] == k:
                stack.pop()
        for count,ch in stack:
            result += (ch * count)
        return result



s = "pbbcggttciiippooaais"
k = 2
print(Solution().func(s,k))
