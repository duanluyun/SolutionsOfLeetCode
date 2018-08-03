class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==1:
            preNode=head
            for i in range(n-1):
                preNode=preNode.next
            newHead=preNode
            pre=None
            preNext=preNode.next
            pNode=head
            while True:
                next=pNode.next
                pNode.next=pre
                if pNode==preNode:
                    break
                pre=pNode
                pNode=next
            head.next=preNext
            return newHead
        else:
            preNode=head
            for i in range(m-2):
                preNode=preNode.next
            pNode=preNode.next
            pre=None
            pNode2=head
            for i in range(n-1):
                pNode2=pNode2.next
            while True:
                next=pNode.next
                pNode.next=pre
                if pNode==pNode2:
                    preNode.next.next=next
                    preNode.next=pNode2
                    break
                pre=pNode
                pNode=next
            return head


