# This is the an algorithm that transpose a matrix

from typing import List
def Transp(matrix:List[List[int]])-> List[List[int]]:
    result = []
    for col in range(len(matrix[0])):
        newArr = []
        for row in range(len(matrix)):
            newArr.append(matrix[row][col])
        result.append(newArr)

    return result

matrix = [
        [1,2,4],
        [2,7,5],
        [9,6,8]
        ]
print(Transp(matrix))
