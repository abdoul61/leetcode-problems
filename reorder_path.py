# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way 
# to travel between two different cities (this network form a tree). Last year, The ministry of transport decided 
# to orient the roads in one direction because they are too narrow.
# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
# It's guaranteed that each city can reach city 0 after reorder.

from typing import List
from collections import deque
from collections import defaultdict
class Solution:
    visited = set()
    graph = defaultdict(dict)
    def __init__(self):
        return None

    def dfs(self,root,count):
        self.visited.add(root)
        for node,value in self.graph[root].items():
            if node not in self.visited:
                if value == 1:
                    count[0] += 1
                self.dfs(node,count)

    def func(self,cities:int,connections:List[List[int]])->int:
        for u,v in connections:
            self.graph[u][v] = 1
            self.graph[v][u] = 0
        count = [0]
        self.dfs(0,count)
        return count[0]


n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(Solution().func(n,connections))

# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
