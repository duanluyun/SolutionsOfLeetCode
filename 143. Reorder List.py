class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None:
            return None
        slow=head
        fast=head.next
        newHead=None

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        pNode=slow.next
        slow.next=None
        pre=None

        while pNode:
            pNodeNext=pNode.next
            pNode.next=pre
            if pNodeNext==None:
                newHead=pNode
                break
            pre=pNode
            pNode=pNodeNext
        p=head
        pre=newHead

        while pre:
            pnext=p.next
            prenext=pre.next
            p.next=pre
            pre.next=pnext
            pre=prenext
            p=p.next.next


node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node6=ListNode(6)



node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6


S=Solution()
head=S.reorderList(node1)
while head:
    print(head.val)
    head=head.next

