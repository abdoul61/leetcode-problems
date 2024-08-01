# You are given a string of length n and k an integer. return 
# The length of the longuest substring of s without repeating a charactere
# You  are allow to change up to k times some charactere of the string



from typing import List

class Solution:
    def __init__(self):
        pass

    def twoPointer(self,s:str,k:int)->int:
        result = 0
        map = {}
        l = 0
        maxFr = 0
        for r in range(len(s)):
            
        #1 count the frequency of each charactere
            map[s[r]] = 1 + map.get(s[r],0)
        #2 adjust the maxfrequency
            maxFr = max(maxFr,map[s[r]])
        #2 check if the window is valid
            while(r-l+1) - maxFr > k:
                #shrink the window
                map[s[l]] -= 1
                l += 1
        #3 update the result
            result = max(result,r-l+1)
        # 4 return the result
        return result




print(Solution().twoPointer("AABABBA",1))


