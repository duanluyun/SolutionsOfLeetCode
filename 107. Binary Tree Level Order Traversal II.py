class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        return self.Traversal(root, res)

    def Traversal(self, root, res):
        if root == None:
            return
        level = [root]
        while level:
            cur = [node.val for node in level]
            res.insert(0, cur)
            level = [child for node in level for child in (node.left, node.right) if child]
        return res