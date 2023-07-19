# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Time complexity of this algorithm is O(n*m) where n,m represent the length of the grid
# Space complexity is linear because all the Node will be save in the set

from typing import List
class Solution:
    visited = set()
    def __init__(self):
        return None
    def dfs(self,i,j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != "1" or (i,j) in self.visited:
            return 
        self.visited.add((i,j))
        self.dfs(i,j+1)
        self.dfs(i,j-1)
        self.dfs(i+1,j)
        self.dfs(i-1,j)


    def numIland(self,grid:List[List[str]])->int:
        value = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in self.visited:
                    self.dfs(i,j)
                    value += 1
        return value

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIland(grid))
# Output: 1
