class Solution:
    def Clone(self, pHead):
        if pHead == None:
            return None
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode
