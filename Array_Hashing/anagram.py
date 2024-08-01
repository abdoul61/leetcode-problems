
#problem statement; find is str t is an anagram of the string s
from typing import List

class Solution:
    def __init__(self):
        pass
    def anagram(self,s:str,t:str)->bool:
        if s == t:
            return True
        if len(t) != len(s):
            return False

        map_t,map_s = {},{}
        for c in s:
            map_s[c] = 1 + map_s.get(c,0)
        for c in t:
            map_t[c] = 1 + map_t.get(c,0) 
        
        for c in map_t.keys():
            if map_t[c] != map_s[c]:
                return False
        return True
