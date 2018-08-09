class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        head=self.connectCopyNode(head)
        head=self.connectRandomPointer(head)
        head=self.ReconnectCopyNode(head)
        return head

    def connectCopyNode(self,head):
        pNode=head
        while pNode:
            CopyNode=RandomListNode(pNode.label)
            next=pNode.next
            pNode.next=CopyNode
            CopyNode.next=next
            pNode=CopyNode.next
        return head

    def connectRandomPointer(self,head):
        pNode=head
        while pNode:
            CopyNode=pNode.next
            if pNode.random!=None:
                CopyNode.random=pNode.random.next
            pNode=CopyNode.next
        return head

    def ReconnectCopyNode(self,head):
        pNode=head
        copyNode=theHead=pNode.next
        pNode.next=copyNode.next
        pNode=pNode.next
        while pNode!=None:
            copyNode.next=pNode.next
            copyNode=copyNode.next
            pNode.next=copyNode.next
            pNode=pNode.next
        return theHead



node1=RandomListNode(1)
node2=RandomListNode(2)
node3=RandomListNode(3)

node1.next=node2
node2.next=node3
node1.random=node3

S=Solution()
head=S.copyRandomList(node1)

print(head.label)
print(head.random.label)
print(head.next.label)
print(head.next.next.label)