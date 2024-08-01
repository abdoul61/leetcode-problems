# In the worst case the time complexity for this algorithm is gonna be 10^4 time and space complexity which is most likely
# 10000
from typing import List
from collections import deque


class Solution:
    def __init__(self):
        return None

    def func(self,deadends:List[str],target:str)->int:
        if "0000" == target:
            return -1
        q = deque()
        cache = set(deadends)
        q.append(["0000",0]) #root and the depth
        
        while q:
                node,depth = q.popleft()
                if node == target:
                    return depth
                else:
                    if node not in cache:
                        cache.add(node)
                        for child in self.generate(node):
                            q.append([child,depth+1])
        
        return -1
    def generate(self,parent)->List[str]:
        result = []
        for i in range(len(parent)):
            p = str((int(parent[i])+1) % 10 )
            result.append(parent[:i] + p + parent[i+1:])
            p = str((int(parent[i]) -1 + 10) % 10)
            result.append(parent[:i] + p + parent[i+1:])
        return result

    
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(Solution().func(deadends,target))






