class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==None or len(matrix)<1 or target==None:
            return False
        numRows=len(matrix)
        numCol=len(matrix[0])
        x=numCol-1
        y=0
        while y<=numRows-1 and x>=0:
            if matrix[y][x]>target:
                x-=1
            elif matrix[y][x]<target:
                y+=1
            else:
                return True
        return False

S=Solution()
print(S.searchMatrix([[1]],1))
