from typing import List



class Solution:
    def __init__(self):
        return None

    def func(self,board:List[List[int]])->List[List[int]]:
        # checking for errors
        if not board:
            return board
        
        is_done = True
        COLS = len(board[0])
        ROW = len(board)
        # Step one tag horizontally all the same numbers
        for r in range(ROW):
            for c in range(len(board[r])-2):
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r][c+1] = -num2
                    board[r][c+2] = -num3
                    is_done = False

        # Step two tag vertically all the same all numbers
        for c in range(COLS):
            for r in range(ROW-2):
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r+1][c] = -num2
                    board[r+2][c] = -num3
                    is_done = False

        
        # Step four apply gravity
        if not is_done:
            for c in range(COLS):
                last_row = ROW-1
                for r in range(ROW-1,-1,-1):
                    if board[r][c] > 0:
                        board[last_row][c] = board[r][c]
                        last_row -= 1
                for r in range(last_row,-1,-1):
                    board[r][c] = 0

        return board if is_done else self.func(board) 
        # Step four collapse all the numbers inside the empty Space
board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314]
        ,[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
print(Solution().func(board))

