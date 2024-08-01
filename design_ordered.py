


from typing import List

class Solution:
    def __init__(self,n:int):
        self.data = [""] * (n + 1)
        self.pointer = 1
        pass


    def insert(self,nkey:int,value:str)->List[str]:
        self.data[nkey] = value

        result = []
        if self.pointer == nkey:
            while self.pointer < len(self.data) and self.data[self.pointer]:
                result.append(self.data[self.pointer])
                self.pointer += 1
        return result





data = [[5,""],[3,"ccccc"],[1,"aaaaa"],[2,"bbbbb"],[5,"eeeee"],[4,"ddddd"]]
for k,v in data:
    print(Solution(6).insert(k,v))
