# Design an algorithm to encode a list of strings to a string. The encoded string is 
#then sent over the network and is decoded back to the original list of strings.




from typing import List


class Solution:

    def __init__(self):
        pass


    def encode(self,words:List[str])->str:
        result = ""
        for w in words:
            l = len(w)
            result += str(l)+ "#"+ w 
        return result

    def decode(self,s:str)->List[str]:
        result = []
        left = 0
        while left < len(s):
            r = left
            while s[r] != "#" :
                r += 1
            length = int(s[left:r])
            result.append(s[r+1: r+1 + length])
            left = r + 1 + length
        return result

    def product_except(self,nums:List[int])->List[int]:
        result = [1] * len(nums)
        prex,suffx = 1,1
        for i in range(len(nums)):
            result[i] = prex
            prex = nums[i] * prex
        for j in range(len(nums)-1,-1,-1):
            result[j] = result[j] * suffx
            suffx *= nums[j]
        return result
    def characterReplacement(self,s:str,k:int)->int:
        my_map = {}
        left = 0
        maxF = 0
        solution = 0
        for right in range(len(s)):
            my_map[s[right]] = 1 + my_map.get(s[right],0)
            #update the maxFrquncy
            maxF = max(maxF,my_map[s[right]])
            
            #check if the window is still valid
            if (right - left + 1) - maxF > k:
                my_map[s[left]] -= 1
                left += 1
            solution = max(solution,(right - left + 1))
        return solution

mystring =  "AABABBA"
k = 1

s = Solution()
print(s.product_except([1,2,3,4]))
print(s.characterReplacement(mystring,k))



