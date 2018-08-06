class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        count=1
        level=[root]
        while level:
            level=[child for node in level for child in(node.left,node.right) if child]
            if not level:
                return count
            count+=1
            for node in level:
                if node.left==None and node.right==None:
                    return count



