"""
先把两个数字用列表表示出来，再转化为int后进行相加，最后构造相加结果的单链表返回即可
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        #遍历两个链表加入到我们构建的字符串变量中
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        #把列表里面的元素转成int，然后反转，加起来，转成字符串，然后再反转
        add = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        #构建链表
        head = ListNode(add[0])
        answer = head
        for i in range(1, len(add)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer
