class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) <= 1:
            return 0
        profits = 0
        for i in range(len(prices) - 1):
            j = i + 1
            if prices[j] > prices[i]:
                profits += (prices[j] - prices[i])
        return profits
