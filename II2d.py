import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        numRows = len(matrix)
        numCols = len(matrix[0])

        row = 0
        col = numCols-1

        while 0<=row<numRows and 0<=col<numCols:
            thisNum = matrix[row][col]
            if thisNum < target:
                row += 1
            elif thisNum > target:
                col -= 1
            else:
                return True

        return False
val=Solution()
n,target=map(int,input().split())
R=n
C=n
nums=list(map(int,input().split()))
matrix=np.array(nums).reshape(R,C)
print(val.searchMatrix(matrix,target))
