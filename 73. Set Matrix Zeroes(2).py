class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        theFirstRowHasZero= not all(matrix[0])
        numRows=len(matrix)
        numCols=len(matrix[0])
        for y in range(1,numRows):
            for x in range(numCols):
                if matrix[y][x]==0:
                    matrix[y][0]=0
                    matrix[0][x]=0

        for y in range(1,numRows):
            for x in range(numCols-1,-1,-1):
                if matrix[y][0]==0 or matrix[0][x]==0:
                    matrix[y][x]=0

        if theFirstRowHasZero:
            matrix[0]=[0]*numCols

        return matrix



