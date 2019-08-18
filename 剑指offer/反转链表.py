"""
定义三个指针，让第二个的next指向第一个
指针2移动到3的位置，指针1移动到2的位置，指针3后移
如此反复，知道指针3指向为空时再进行最后一次反转
"""
class Solution:
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        #上一个节点
        pre = None
        while pHead:
            #暂存当前节点的下一个节点信息
            temp = pHead.next
            #反转节点
            pHead.next = pre
            #进行下一个节点
            pre = pHead
            pHead = temp
        return pre
            
