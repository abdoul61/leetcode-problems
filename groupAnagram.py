# This is a leetcode problem called group Anagram:
#Difficulty: Medium

from collections import defaultdict
from typing import List
def fn(strs: List[str])->List[List[str]]:
    seen = defaultdict(list)
    for s in strs:
        # The reason why i intialized this with 26 is because the alphabet can only have 26 different letters max
        count = [0] * 26
        for c in s:
            # ord(c) gives you the aski value of the character c 
            # and to have the index where it belongs to you can remove the smallest letter of the alphabet which is a that is why i used ord(c) - ord("a")
             
            count[ord(c) - ord("a")] += 1
        
        # print(tuple(count)) for debug purpose
        # changing count to tuple because we cant use list as key for hashmap or dict in python 
        seen[tuple(count)].append(s)
         
    # print(seen) for debug purpose 
    return seen.values()

print(fn(["eat","tea","tan","ate","nat","bat"]))
# The Time complexity here is m * n , m is length of list strs and n is the length of the average string s

