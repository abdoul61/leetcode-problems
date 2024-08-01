# Leetcode problem called the longuest substring without repeating characters



def fn(s:str)-> int:
    seen = {}
    max_count = 0
    r = 0
    l = 0
    while l < len(s) and r < len(s):
        el = s[r]
        if el in seen:
            l = max(l, seen[el]+1)
        seen[el] = r
        max_count = max(max_count, r-l+1)
        r += 1
    return max_count



print(fn("abcabcbb"))
print(fn("bbbbb"))
print(fn("pwwkew"))
