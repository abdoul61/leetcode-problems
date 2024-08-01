from typing import List
from collections import defaultdict


class Solution:

    def __init__(self):
        return None

    def func(self,pre:List[List[int]],n:int) -> List[int]:
        cache = set()
        result = []
        seen = set()
        adJMap = defaultdict(list)
        for crs,pres in pre:
            adJMap[crs].append(pres)

        def DFS(crs):
            if crs in cache:
                return False
            if crs in seen:
                return True
            cache.add(crs)
            for child in adJMap[crs]:
                if not DFS(child):
                    return False
            cache.remove(crs)
            seen.add(crs)
            result.append(crs)
            return True
        for crs in range(len(pre)):
            if DFS(crs) == False:
                return []
        
        print(seen)
        return result




data = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().func(data,4))



