class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        if root==None:
            return res
        res=self.traversal(root,sum,[],res)
        return res

    def traversal(self,root,target,temp,res):
        if root.left==None and root.right==None:
            if root.val==target:
                temp+=[root.val]
                res.append(temp)
            return res
        if root.left:
            self.traversal(root.left,target-root.val,temp+[root.val],res)
        if root.right:
            self.traversal(root.right,target-root.val,temp+[root.val],res)
        return res

