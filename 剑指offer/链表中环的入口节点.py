"""
环的概念就是最后回到了原点
遍历链表把每个元素记录在list里
然后一旦遇到重复节点则存在环
"""
class Solution:
    def EntryNodeOfLoop(self, pHead):
        lis = []
        #遍历，然后不停加入到lis
        #知道节点重复
        while pHead:
            if pHead in lis:
                return pHead
            lis.append(pHead)
            pHead = pHead.next
        return None
