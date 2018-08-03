# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        ls = [i for i in range(1, n + 1)]
        return self.helper(ls)

    def helper(self, ls):
        if len(ls) == 0:
            return [None]
        res = []
        for i in range(len(ls)):
            for left in self.helper(ls[:i]):
                for right in self.helper(ls[i + 1:]):
                    node, node.left, node.right = TreeNode(ls[i]), left, right
                    res += [node]
        return res
