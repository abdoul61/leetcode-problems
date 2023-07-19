
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] 
# represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring 
# cells directly north, south, east, and west if the neighboring cell's height is less than or
# equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


from typing import List

class Solution:
    pacificSet = set()
    atlanticSet = set()
    def __init__(self):
        return None
    def dfs(self,r,c,mp,prevH,grid):
        if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in mp or grid[r][c] < prevH:
            return
        mp.add((r,c))
        self.dfs(r+1,c,mp,grid[r][c],grid)
        self.dfs(r-1,c,mp,grid[r][c],grid)
        self.dfs(r,c+1,mp,grid[r][c],grid)
        self.dfs(r,c-1,mp,grid[r][c],grid)
        
    def func(self,grid:List[List[int]])->List[List[int]]:
        result = []
        for r in range(len(grid)):
            self.dfs(r,0,self.atlanticSet,grid[r][0],grid)
            self.dfs(r,len(grid[0])-1,self.pacificSet,grid[r][len(grid[0])-1],grid)

        for c in range(len(grid[0])):
            self.dfs(0,c,self.atlanticSet,grid[0][c],grid)
            self.dfs(len(grid)-1,c,self.pacificSet,grid[len(grid)-1][c],grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in self.pacificSet and (i,j) in self.atlanticSet:
                    result.append([i,j])
        return result




heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().func(heights))
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

