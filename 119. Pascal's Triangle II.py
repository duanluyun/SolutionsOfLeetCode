class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex<0:
            return []
        res=[[1],[1,1]]
        if rowIndex<=1:
            return res[0] if rowIndex<1 else res[1]
        temp=[1,1]
        for i in range(2,rowIndex+1):
            res=[1]*(i+1)
            for j in range(1,len(res)-1):
                res[j]=temp[j-1]+temp[j]
            temp=res
        return res

