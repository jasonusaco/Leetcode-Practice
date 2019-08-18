"""
方法1：最直接的蛮力法，遍历第一个链表，每个结点，都把第二个扫一遍，
找到公共结点。复杂度O(mn)。

方法2：因为从第一个公共节点开始，后面都是公共节点了，所以借助两个栈，
把两个链表从后往前比较，最后一个相同节点就是我们要找的节点，
栈顶元素都一样就pop出去，直到最后一个相同元素
时间为O(m+n)，但是会额外空间

方法3：先遍历两个链表得到长度，如果m>n，则m表先走m-n步，然后两个链表
再同时走，直到找到第一个相同节点，
复杂度为O(m+n),且不需要额外空间
"""
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        length1 = self.GetLength(pHead1)
        length2 = self.GetLength(pHead2)

        #先确定哪个更长，来看谁先走
        if length1 > length2:
            headLong = pHead1
            headShort = pHead2

        else:
            headLong = pHead2
            headShort = pHead1
        #先走的步数
        diff = abs(length1-length2)

        for i in range(diff):
            #长的链表先走m-n步
            headLong = headLong.next

        while headLong != None and headShort != None and headLong != headShort:
            headLong = headLong.next
            headShort = headShort.next
        return headLong
    
    #获取长度函数，遍历pHead
    def GetLength(self, pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length
        
