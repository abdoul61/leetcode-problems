# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



from typing import List
from collections import deque
class Solution:
    def __init__(self):
        return None

    

    def func(self,grid:List[List[int]])-> int:
        count = 0
        fresh = 0
        que = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append([i,j])
                if grid[i][j] == 1:
                    fresh += 1
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while que and fresh > 0:
            for i in range(len(que)):
                r,c = que.popleft()
                for dr,dc in directions:
                    row,col = dr+r,dc+c
                    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    que.append([row,col])
                    fresh -= 1
            count += 1
        return count if fresh == 0 else -1









grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().func(grid))
# Output: 4
