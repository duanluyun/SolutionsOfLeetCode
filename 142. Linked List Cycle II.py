class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        slow=head
        fast=head.next
        meetNode=self.meet(slow,fast)
        if meetNode==None:
            return None
        length=self.len(meetNode)
        return self.entricy(head,length)

    def meet(self,slow,fast):
        try:
            while slow is not fast:
                slow=slow.next
                fast=fast.next.next
            return slow
        except:
            return None

    def len(self,node):
        pNode=node
        preNode=node.next
        count=1
        while preNode!=pNode:
            preNode=preNode.next
            count+=1
        return count

    def entricy(self,head,length):
        slow=head
        fast=head
        for  i in range(length):
            fast=fast.next
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow