# you are given two string s1, s2 you are asked to check if s1 permutation 
# is part of the s2: return true else retuen false

class Solution:
    def __init__(self):
        pass


    def stringPerm(self,s1:str,s2:str)->bool:
        # check if s2 is bigger enought to contains s1
        if len(s1) > len(s2):
            return False

        # check if s1 appear in s2 
        if s1 in s2 or s1[::-1] in s2:
            return True

        r = 0
        l = len(s1)
        while r < len(s2) and l <= len(s2):
            newString = s2[r:l]
            if self.compareString(s1,newString):
                return True
            l += 1
            r += 1

        return False

    def compareString(self,s1:str,s2:str)->bool:
        array1 = [0] * 26
        array2 = [0] * 26
        for i in range(len(s1)):
            a = ord(s1[i])
            b = ord(s2[i])
            array1[ord('a')-a] += 1
            array2[ord('a') - b] += 1
        return array1 == array2



s = Solution()
print(s.stringPerm("ab","eidbaooo"))
print(s.stringPerm("ab","eidboaoo"))
print(s.stringPerm("hello","ooolleoooleh"))
print(s.stringPerm("adc","dcda"))
print(s.stringPerm("abc","bbbca"))


