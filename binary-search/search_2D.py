from typing import List
# The number are sorted in the vertical form and in the horizontal form
def search2D(matrix:List[List[int]],target:int)->bool:
    # Col represent the first column of the matrix
    COL = len(matrix[0])
    # ROW represent the last row of the maxtrix
    ROW = len(matrix)
    # top and bottom are the first row and last row index
    top,bot = 0,ROW-1

    while top <= bot:
        # Let find the row where the target could be in case it exist
        row = (top + bot)//2
        if matrix[row][0] > target:
            bot = row -1
        elif matrix[row][-1] < target:
            top = row + 1
        else:
            break
        if not top <= bot:
            return False

        row = (top + bot)//2

        l,r = 0, COL-1

        while l <= r:
            m = (l+r)//2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1

        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(search2D(matrix,target))






