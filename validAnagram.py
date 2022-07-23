# This is a leetcode problem called valid anagram


from ast import Str


def fn(s: str,t:str) -> bool:
# or you can also resolve this problem by just sorting  the two string 
# such as return sorted(s) == sorted(t) 
# but this  the time complexity of the sorted algo is nlog(n) with n the length of of string s 
    if(len(s) != len(t)):
        return False
    seen , seent = {},{}
    for i in range(len(s)):
        seen[s[i]] = seen.get(s[i],0)+ 1
        seent[t[i]] = seent.get(t[i],0) + 1
    
    for el in seen:
        if seent.get(el,0) != seen.get(el,0):
            return False
    
    return True


s = "anagram"
t = "nagaram"
print(fn(s,t))
