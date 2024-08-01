# solution is linear time complexity




from typing import List


class Solution:

    def __init__(self):

        return None

    def decode(self,s:str)->str:

        stack = []
        for i in range(len(s)):

            if s[i] != "]":
                stack.append(s[i])
            else:

                substring = ""
                while stack and stack[-1] != "[":
                    substring = substring + stack.pop()
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substring)

        return "".join(stack)


s = ["3[a]2[bc]","3[a2[c]]"]
for el in s:
    print(Solution().decode(el))

