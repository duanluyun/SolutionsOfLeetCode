class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l=0
        r=x
        while r>=l:
            middle=(r+l)//2
            if middle*middle<=x  and (middle+1)**2>x:
                return middle
            elif middle**2<x:
                l=middle+1
            elif middle**2>x:
                r=middle

