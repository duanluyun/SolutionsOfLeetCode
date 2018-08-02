class Solution:
    def combaine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        temp=[]
        res=[]
        x=1
        while True:
            if len(temp)==k:
                res.append(temp[:])
            if x>n or len(temp)==k:
                if len(temp)==0:
                    return res
                else:
                    x=temp.pop()+1
            else:
                temp.append(x)
                x+=1
S=Solution()
print(S.combaine(4,3))


