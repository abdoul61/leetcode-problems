#This is a leetcode problem called the valid palindrome


from typing import List

def fn(stn :str)-> bool:
    # First convert all the charactere to lower case
    # The  remove all the space and special characters
    s = ""
    stn2 = stn.lower()
    stn2 = stn2.replace(" ","")
    for el in stn2:
        if isValid(el):
            s += el 
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def isValid(ch):
    if ch.isalnum():
        return True
    return False


s = "A Man, a Plan, a canal:b Panama"

print(fn(s))
