# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.




from typing import List
class Solution:
    def __init__(self):
        return None

    def dfs(self,i,j,grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != "O":
            return
        grid[i][j] = "T"
        self.dfs(i,j+1,grid)
        self.dfs(i,j-1,grid)
        self.dfs(i+1,j,grid)
        self.dfs(i-1,j,grid)
    
    def func(self,grid:List[List[str]])->None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and (i in [0,len(grid)-1] and j in [0,len(grid[0])-1]):
                    self.dfs(i,j,grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    grid[i][j] = "X"

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "T":
                    grid[i][j] = "O"
        
        print(grid)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(Solution().func(board))
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
