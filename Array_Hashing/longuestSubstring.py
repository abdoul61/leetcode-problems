# Given a string and they will ask you to find the 
# longuest substring of string without duplicate
# of charactere




class Solution:
    def __init__(self):
        pass

    def longuest(self,s:str)->int:
        result = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r-l+1)
        return result
    

s = "abcabcbb"
print(Solution().longuest(s))
