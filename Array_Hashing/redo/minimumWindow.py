# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring
# of s such that every character in t (including duplicates) is included in the window. If there is no 
# such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
#  
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
from collections import Counter

class Solution:
    def __init__(self):
        pass

    def function(self,s:str,t:str)->str:
        window = [-1,-1]
        m1 = {}
        for c in t:
            m1[c] = 1 + m1.get(c,0)
        m2 = {} 
        l = 0
        windowL = float("infinity")
        need = len(m1)
        have = 0
        for r in range(len(s)):
            m2[s[r]] = 1 + m2.get(s[r],0)
            if s[r] in m1 and m2[s[r]] == m1[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < windowL:
                    windowL = (r - l + 1)
                    window = [l ,r]
                m2[s[l]] -= 1
                if s[l] in m1 and m2[s[l]] < m1[s[l]]:
                    have -= 1
                l += 1
        l,r = window
        return s[l:r + 1] if windowL != float("infinity") else ""



s = Solution()
print(s.function("ADOBECODEBANC","ABC"))
