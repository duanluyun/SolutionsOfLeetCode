# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        level=[root]
        while level:
            cur=[node.val for node in level]
            res.append(cur)
            level=[child for node in level for child in (node.left,node.right) if child]
        return len(res)