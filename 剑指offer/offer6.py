"""
将链表中的值记录到list中，然后进行翻转list
"""
class Solution:
    def printListFromTaliToHead(self, listNode):
        lis = []
        while listNode:
            lis.append(listNode.val)
            listNode = listNode.next
        return lis[::-1]
        
