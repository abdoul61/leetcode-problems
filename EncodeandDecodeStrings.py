#This  a leetcode problem called encode and decode strings
# We are prompted to write two function one to encode and another to decode


from typing import List

def fn(ls: List[str])-> List[str]:
    s = ""
    for w in ls:
        l = len(w)
        s += str(l) + "#" + w 
    return s 


def decod(s:str)-> List[int]:
    res = []
    i = 0
    while i < len(s):
        j = i 
        while s[j] != "#":
            j  = j + 1
        
        length = int(s[i:j])
        w = s[j + 1: j+ 1 + length]
        res.append(w)
        i = j + 1 + length 
    return res 


ls = fn(["hello","world"])
print(ls)
print()
print(decod(ls))
