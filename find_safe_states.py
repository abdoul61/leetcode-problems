from typing import List
# from collections import deque
from collections import defaultdict

class Solutions:
    safe = {}
    def __init__(self):
        return None

    def func(self,graph:List[List[int]])->List[int]:
        result = []
        for i in range(len(graph)):
            if self.DFS(graph[i],graph):
                result.append(graph[i])
        return result 


    def DFS(self,node,graph)->bool:
        # Check if the current element himself is visited already
        if node in self.safe: 
            return self.safe[node]
        # since he is not visited yet let assigner him a false value until proverd otherwise
        self.safe[node] = False
        # for him to be validated all his childreen need to be validaded
        for child in graph[node]:
            # check if any of his childreen is visited already and is not safe
            if not self.DFS(child,graph):
                # then invalide the the node as well
                return self.safe[child]
        # At this point none of his childreen has been invalidated
        # therefore change his value to true and return his value as well
        self.safe[node] = True
        return self.safe[node]


graph = [[1,2],[2,3],[5],[0],[5],[],[]]

print(Solutions().func(graph))
