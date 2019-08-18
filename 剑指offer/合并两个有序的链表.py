"""
方法1：转成两个list，排序，然后再并入链表
"""
class Solution:
    def Merge(self, pHead1, pHead2):
        if pHead1 is None and pHead2 is None:
            return None

        num1 = []
        num2 = []

        #遍历链表1，把值全部放入num1
        while pHead1:
            num1.append(pHead1.val)
            pHead1 = pHead1.next

        while pHead2:
            num2.append(pHead2.val)
            pHead2 = pHead2.next

        #合并以后的列表
        ans = num1+num2
        ans.sort()

        #重新把合并后的列表加入到链表中
        #先定义头结点
        head = ListNode(ans[0])
        #一开始没有pre，所以等于head
        pre = head
        for i in range(1, len(ans)):
            node = ListNode(ans[i])
            pre.next = node
            pre = pre.next
        return head

"""
方法2，递归
"""
class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not phead2:
            return pHead1
        #新链表的头结点
        head = None
        #如果链表1的值比链表2的小
        #那么那么头结点就去链表1的第一个值
        if pHead1.val < pHead2.val:
            head = pHead1
            #递归重复此过程
            head.next = self.Merge(pHead1.next, pHead2)

        else:
            head = pHead2
            head.next = self.Merge(pHead1, pHead2.next)
        return head
