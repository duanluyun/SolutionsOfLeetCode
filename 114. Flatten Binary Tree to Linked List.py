# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self,root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        res=[]
        res=self.Inorder(root,res)
        pre=None
        for node in res:
            node.left=None
            if pre!=None:
                pre.right=node
            pre=node



    def Inorder(self,root,res):
        if root.left==None and root.right==None:
            res.append(root)
            return res
        res.append(root)
        if root.left:
            self.Inorder(root.left,res)
        if root.right:
            self.Inorder(root.right,res)
        return res

node1=TreeNode(1)
node6=TreeNode(6)
node2=TreeNode(2)
node5=TreeNode(5)
node3=TreeNode(3)
node4=TreeNode(4)

node1.left=node2
node1.right=node5
node2.left=node3
node2.right=node4
node5.right=node6

S=Solution()
head=S.flatten(node1)
while head:
    print(head.val)
    head=head.right