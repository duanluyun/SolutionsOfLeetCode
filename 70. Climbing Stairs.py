class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return 0
        one=1
        two=2
        if n<=2:
            return one if n==1 else two
        for i in range(n-2):
            three=one+two
            one=two
            two=three
        return three
