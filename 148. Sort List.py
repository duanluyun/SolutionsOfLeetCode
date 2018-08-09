class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        newhead=slow.next
        slow.next=None
        l=self.sortList(head)
        r=self.sortList(newhead)
        return self.merge(l,r)

    def merge(self,l,r):
        if l==None or r==None:
            return l or r
        if l.val>r.val:
            l,r=r,l
        head=pre=l
        l=l.next
        while l and r:
            if l.val<r.val:
                l=l.next
            else:
                next=pre.next
                tempnext=r.next
                pre.next=r
                r.next=next
                r=tempnext
            pre=pre.next
        pre.next=l or r
        return head
