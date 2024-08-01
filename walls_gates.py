from typing import List
from collections import deque
class Solution:

    def __init__(self,rooms:List[List[int]]):
        self.rooms = rooms
        return None

    def func(self)->List[List[int]]:
       cache = set()
       q = deque()
       dist = 0
       directions = [[0,1],[1,0],[0,-1],[-1,0]]
       for i in range(len(self.rooms)):
           for j in range(len(self.rooms[0])):
               if self.rooms[i][j] == 0:
                   cache.add((i,j))
                   q.append([i,j])
       
       while q:
           for i in range(len(q)):
               r,c = q.popleft()
               if r < 0 or r == len(self.rooms) or c < 0 or c == len(self.rooms[0]) or self.rooms[r][c] == -1 or (r,c) in cache:
                   return []
               if self.rooms[r][c]:
                   self.rooms[r][c] = dist
                   cache.add((r,c))
               for dr,dc in directions:
                    row,col = dr + r,dc + c
                    q.append([row,col])
               dist += 1
       return self.rooms
       

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print(Solution(rooms).func())
