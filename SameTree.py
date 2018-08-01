# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        if p==None and q!=None or p!=None and q==None:
            return False
        if p.val==q.val:
            if self.check(p,q):
                return True
            return False
        else:
            return False

    def check(self,p,q):
        if p==None and q==None:
            return True
        if (p==None and q!=None) or (q==None and p!=None):
            return False
        if p.val!=q.val:
            return False
        return self.check(p.left,q.left) and self.check(p.right,q.right)

# node1=TreeNode(1)
# node2=TreeNode(2)
# node3=TreeNode(3)
# node1.left=node2
# node1.right=node3
#
# node4=TreeNode(1)
# node5=TreeNode(2)
# node6=TreeNode(5)
# node4.left=node5
# node4.right=node6

S=Solution()
print(S.isSameTree(node1,node4))
