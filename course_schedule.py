from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        return None

    def func(self,pre:List[List[int]],numCourse:int)->bool:

        course_seen = set()
        # map all the courses from a adjacent list
        adjMap = defaultdict(list)
        for crs,preq in pre:
            adjMap[crs].append(preq)
        
        def DFS(crs):
            ###### ########################
            # Conditions 
            ##############################
            if adjMap[crs] == []:
                return True
            if crs in course_seen:
                return False

            ##############################3
            # Keep Tracking  operations being done
            #############################
            course_seen.add(crs)

            ###################################
            # Get all the Node childs and run recursively the same function
            #################################################
            for child in adjMap[crs]:
                if not DFS(child):
                    return False
            course_seen.remove(crs)
            adjMap[crs] = []
            return True

        for crs in range(len(pre)):
            if not DFS(crs):
                return False
        return True





pre = [[1,0]]
print(Solution().func(pre,2))
