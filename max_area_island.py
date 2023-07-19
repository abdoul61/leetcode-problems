# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.


from typing import List
class Solution:
    visited = set()
    def __init__(self):
        return None
    def dfs(self,i,j,grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or (i,j) in self.visited:
            return 0
        self.visited.add((i,j))
        return 1 + self.dfs(i+1,j,grid) + self.dfs(i-1,j,grid) + self.dfs(i,j+1,grid) + self.dfs(i,j-1,grid)

    def max_area(self,grid:List[List[int]])->int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited and grid[i][j] == 1:
                    max_area = max(max_area,self.dfs(i,j,grid))
        return max_area








grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().max_area(grid))
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

