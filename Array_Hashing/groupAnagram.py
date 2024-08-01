# given a list of strings and you should group them 
# according if they are anagram
from typing import List

class Solution:
    def __init__(self):
        pass
    def groupAnagram(self,strs:List[str])->List[List[str]]:
        response = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in response:
                response[sorted_s] = []
                response[sorted_s].append(s)
            else:
                response[sorted_s].append(s)
        return list(response.values())

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print(s.groupAnagram(strs))
