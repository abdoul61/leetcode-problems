# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a
# group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
# Return the number of islands in grid2 that are considered sub-islands.


from typing import List
class Solution:
    visited = set()
    def __init__(self):
        return None
    def dfs(self,i,j,grid1,grid2):
        result = True
        if i < 0 or j < 0 or i == len(grid2) or j == len(grid2[0]) or grid2[i][j] == 0 or (i,j) in self.visited:
            return True
        if grid1[i][j] == 0:
            result = False
            
        self.visited.add((i,j))
        result = self.dfs(i,j+1,grid1,grid2) and result
        result = self.dfs(i,j-1,grid1,grid2) and result
        result = self.dfs(i-1,j,grid1,grid2) and result 
        result = self.dfs(i+1,j,grid1,grid2) and result
        return result



    def count_sub_island(self,grid1:List[List[int]],grid2:List[List[int]])->int:
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in self.visited and self.dfs(i,j,grid1,grid2):
                    count += 1


        return count










grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(Solution().count_sub_island(grid1,grid2))
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
