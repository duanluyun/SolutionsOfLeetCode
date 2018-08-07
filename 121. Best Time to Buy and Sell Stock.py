class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==None or len(prices)==1:
            return 0
        res=[]
        for i in range(len(prices)):
            j=len(prices)-1
            while j>i:
                if prices[j]==prices[j-1]:
                    j-=1
                    continue
                elif prices[j]>prices[i]:
                    res.append(prices[j]-prices[i])
                j-=1
        return max(res)

