


class Node:
    def __init__(self,val=0,neighbords=None):
        self.val = val
        self.neighbords = neighbords if neighbords is not None else []


class Solution:
    map = {}
    def __init__(self):
        return None

    def dfs(self,node:Node):
        if node in self.map:
            return self.map[node]
        value = node.val
        cp = Node(value)
        self.map[node] = cp
        for nhg in node.neighbords:
            cp.neighbords.append(self.dfs(nhg))

        return cp

    def cloneGraph(self,node:Node)->Node:
        return self.cloneGraph(node) if node else None


adjList = [[2,4],[1,3],[2,4],[1,3]]
print(Solution().cloneGraph(adjList))
