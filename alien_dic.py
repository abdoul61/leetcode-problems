# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a
# different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and
# only if the given words are sorted lexicographically in this alien language.
# Time complexity is linear O(n) where n is the number of string and the space complexity is O(m) where m is the length of the order
from typing import List

class Solution:
    def isAlienSorted(self,words:List[str],order:str)->bool:
        map = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if map[w1[j]] > map[w2[j]]:
                        return False
                    break

        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words,order))
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
