class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        tempres=[]
        tempres=self.traversal(root,'',tempres)
        res=0
        for i in tempres:
            res+=int(i)
        return res

    def traversal(self,root,path,res):
        if root.left==None and root.right==None:
            path+=str(root.val)
            res.append(path)
            return res
        if root.left:
            self.traversal(root.left,path+str(root.val),res)
        if root.right:
            self.traversal(root.right,path+str(root.val),res)
        return res


