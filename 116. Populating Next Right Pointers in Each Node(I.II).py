class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root==None:
            return None
        res=[]
        level=[root]
        while level:
            res.append(level)
            level=[child for node in level for child in (node.left,node.right) if child]
        for l in res:
            for i in range(len(l)-1):
                l[i].next=l[i+1]
            



