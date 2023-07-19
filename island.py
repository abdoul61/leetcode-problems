# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely
# surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the
# island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


##### Time complexity is O(n) and space complexity is i will visited all the node from the grid
from typing import List
class Solution:
    visited = set()
    def __init__(self):
        return None

    def getIslanPerimeter(self,grid:List[List[int]])->int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.dfs(i,j)
        return 0

    def dfs(self,i,j):
        if i <  0 or j < 0 or i == len(grid) or j ==len(grid[0])or grid[i][j] == 0:
            return  1
        if(i,j) in self.visited:
            return 0
        self.visited.add((i,j))
        count = self.dfs(i+1,j)
        count += self.dfs(i-1,j)
        count += self.dfs(i,j-1)
        count += self.dfs(i,j+1)
        return count
        



grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().getIslanPerimeter(grid))
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
