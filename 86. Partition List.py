class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1=pNode1=ListNode(0)
        h2=pNode2=ListNode(0)
        while head:
            if head.val<x:
                pNode1.next=head
                pNode1=pNode1.next
            else:
                pNode2.next=head
                pNode2=pNode2.next
            head=head.next

        pNode1.next=h2.next
        pNode2.next=None
        return h1.next

