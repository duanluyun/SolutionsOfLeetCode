# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        a=[1,2,3]
        b=[4]
        # a.append(b) //a=[1, 2, 3, [4]]
        # a+=b  //a=[1,2,3,4]



S=Solution()
S.flatten()
