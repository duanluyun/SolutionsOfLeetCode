# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.next==None:
            return head

        pNode=head
        preNode=head.next
        while preNode.next!=None:
            while preNode.next!=None and preNode.val==pNode.val:
                preNode=preNode.next
            pNode.next=preNode
            pNode=pNode.next
            if preNode==None:
                return head
            preNode=preNode.next
        return head

node1=ListNode(1)
node2=ListNode(1)
node3=ListNode(2)
node4=ListNode(3)
node5=ListNode(3)


node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5


S=Solution()
head=S.deleteDuplicates(node1)
while head:
    print(head.val)
    head=head.next

