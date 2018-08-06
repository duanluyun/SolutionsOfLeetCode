class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        res1=[]
        res1=self.LeftMiddleRight(root,res1)
        res2=[]
        res2=self.RightMiddleLeft(root,res2)
        return res1==res2

    def LeftMiddleRight(self,root,res):
        if root==None:
            return
        if root.left==None and root.right==None:
            res.append(root.val)
            return res
        if root.left:
            self.LeftMiddleRight(root.left,res)
        res.append(root.val)
        if root.right:
            self.LeftMiddleRight(root.right,res)
        return res

    def RightMiddleLeft(self,root,res):
        if root==None:
            return
        if root.left==None and root.right==None:
            res.append(root.val)
            return res
        if root.right:
            self.RightMiddleLeft(root.right,res)
        res.append(root.val)
        if root.left:
            self.RightMiddleLeft(root.left,res)
        return res


