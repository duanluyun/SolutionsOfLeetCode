class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        req=[]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x]==0:
                    req.append([y,x])
        Row=[]
        for i in req:
            if i[0] in Row:
                continue
            else:
                Row.append(i[0])
        Col=[]
        for i in req:
            if i[1] in Col:
                continue
            else:
                Col.append(i[1])
        for i in Row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in Col:
            for j in range(len(matrix)):
                matrix[j][i]=0




