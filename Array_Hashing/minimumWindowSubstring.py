# You are given two string s and t and are asked to find the minimum s substring that would hav
# the string t.



from typing import List


class Solution:
    def __init__(self):
        pass


    def minimumSub(self,s:str,t:str)->str:
        # a map to count the frequency of t
        if len(s) == 0:
            return ""
        countT,window = {},{}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have = 0
        need = len(t)
        resultL = float("infinity") 
        result = [-1,-1]
        
        l = 0
        for r in range(len(s)):
            # add the new char to the window
            c = s[r]
            window[c] = 1 + window.get(c,0)

            # check if the new char is a valid and if the condition have been meet
            if c in countT and window[c] == countT[c]:
                have += 1

            # making sure that the window is still valid if the condition is meet

            while have == need:
                if (r-l+1) < resultL:
                    result = [l ,r]
                    resultL = (r-l+1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = result
        result = s[l:r+1]
        return result if resultL != float("infinity") else ""

print(Solution().minimumSub("ADOBECODEBANC","ABC",))

