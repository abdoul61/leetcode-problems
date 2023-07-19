# This is the implementation of Graph data structure
# Here we will use the Adjacent matrix representation
# space complexity is O(N * N)
# insert, remove , O(1)


import numpy as np
import queue as Q

class Graph:
    def __init__(self,vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices,vertices))
        self._visited = [0] * self._vertices
        

    def insert_edge(self,u,v,x=1):
        self._adjMat[u][v] = x
    
    def remove_edge(self,u,v):
        self._adjMat[u][v] = 0

    def exist_edge(self,u,v) -> bool:
        return self._adjMat[u][v] != 0


    def vertex_count(self) -> int:
        return self._vertices

    def edge_count(self) -> int:
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count = count + 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i,end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,'--',j)


    def outdegree(self,v) -> int:
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count += 1
        return count


    def indegree(self,v) -> int:
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count = count + 1
        return count 

# Method to traverse the entire graph node by node 
# Breath-First-Search
    def Breath_First_search(self,s):
        i = s
        q = Q.Queue()
        visited = [0] * self._vertices
        print(i,end=' ')
        visited[i] = 1
        q.put(i)

        while not q.empty():
            e = q.get()
            for j in range(self._vertices):
                if self._adjMat[e][j] == 1 and visited[j] == 0:
                    print(j,end=' ')
                    q.put(j)
                    visited[j] = 1

# Depth-Fisrt-search Alogrithm
    def Depth_First_search(self,s):
        if self._visited[s] == 0:
            print(s,end=' ')
            self._visited[s] = 1
            for j in range(self._vertices):
                if self._adjMat[s][j] == 1 and self._visited[j] == 0:
                    self.Depth_First_search(j)

# Method to print the entire graph
    def display_adjMat(self):
        print(self._adjMat)



G = Graph(7)
G.insert_edge(0,1)
G.insert_edge(0,5)
G.insert_edge(0,6)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(1,5)
G.insert_edge(1,6)
G.insert_edge(2,3)
G.insert_edge(2,4)
G.insert_edge(2,6)
G.insert_edge(3,4)
G.insert_edge(4,2)
G.insert_edge(4,5)
G.insert_edge(5,2)
G.insert_edge(5,3)
G.insert_edge(6,3)
G.display_adjMat()

# print('BFS')
# G.Breath_First_search(0)
# print()

# G.Breath_First_search(4)
# print()

print('DFS')
G.Depth_First_search(4)











































