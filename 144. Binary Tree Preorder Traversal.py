class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        res=[]
        res=self.traversal(root,res)
        return res

    def traversal(self,root,res):
        if root.left==None and root.right==None:
            res.append(root.val)
            return res
        res.append(root.val)
        if root.left:
            self.traversal(root.left,res)
        if root.right:
            self.traversal(root.right,res)
        return res

