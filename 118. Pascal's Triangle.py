class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<1:
            return []
        res=[[1],[1,1]]
        if numRows<=2:
            return [res[0]] if numRows==1 else res
        for i in range(3,numRows+1):
            temp=[1]*i
            for j in range(1,len(temp)-1):
                temp[j]=res[i-2][j-1]+res[i-2][j]
            res.append(temp)
        return res

