class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls=[chr(i) for i in range(ord('A'),ord('Z')+1)]
        res=[]
        numList=list(s)
        for i in range(len(s)):
            res.append(ls[int(s[i])])
