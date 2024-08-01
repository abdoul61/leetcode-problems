# given a string check if the string is an palindrom



from typing import List


class Solution:
    def __init__(self):
        pass

    def isPalindrom(self,s:str)->bool:
        lst = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        s = s.replace(" ","")
        for c in s:
            if c not in lst:
                s = s.replace(c,"")
        l,r = 0,len(s)-1
        while l <=r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrom(s))
