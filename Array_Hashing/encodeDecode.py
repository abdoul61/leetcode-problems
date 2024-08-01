# Givin an array of strings, you should be able to encode
# and decode the strings



from typing import List

class Solution:
    def __init__(self):
        pass

    def encode(self,words:List[str])->str:
        result = ""
        for s in words:
            result += str(len(s)) + "#" + s
        return result

    def decode(self,hash:str)->List[str]:
        result = []         
        i = 0
        while i < len(hash):
            j = i
            while hash[j] != "#":
                j += 1
            length = int(hash[i:j])
            word = hash[j+ 1: j+1 + length]
            result.append(word)
            i = j + 1 + length
            
        return result



words = ["Hello","world"]

s = Solution().encode(words)
print(Solution().decode(s))
