# This a leetcode problem called valid soduko 
import collections
from typing import List
col =  collections.defaultdict(set)
row = collections.defaultdict(set)
square = collections.defaultdict(set)
print(col)
print()
print(row)
def fn(board:List[List[str]]) -> bool:
    for i in range(9):
        for k in range(9):
            if board[i][k] == ".":
                continue 
            if board[i][k] in col[i] or board[i][k] in row[k] or board[i][k] in square[(i//3,k//3)]:
                return False
            print(col)
            print(row)
            col[i].add(board[i][k])
            row[k].add(board[i][k])
            square[(i//3,k//3)].add(board[i][k])
    return True
            



print(fn([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))