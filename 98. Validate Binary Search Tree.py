# # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        res=[]
        res=self.InorederTraversal(root,res)
        for i in range(len(res)-1):
            if res[i+1]<=res[i]:
                return False
        return True


    def InorederTraversal(self,root,res):
        if root.left==None and root.right==None:
            res.append(root.val)
            return res
        if root.left:
            self.InorederTraversal(root.left,res)
        res.append(root.val)
        if root.right:
            self.InorederTraversal(root.right,res)
        return res

node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node2.left=node1
node2.right=node3

S=Solution()
print(S.isValidBST(node2))
