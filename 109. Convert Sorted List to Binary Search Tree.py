# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
            return None
        if head.next == None:
            return (TreeNode(head.val))
        pNode=head
        preNode=head.next.next
        while preNode and preNode.next:
            pNode=pNode.next
            preNode=preNode.next.next
        root=TreeNode(pNode.next.val)
        next=pNode.next.next
        pNode.next=None
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(next)
        return root

