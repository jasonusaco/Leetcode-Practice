"""
首先创建一个None节点prev, 然后依次取出原来链表中的元素curr，
添加到prev节点的前面(即将取出的curr节点的next节点设置为prev)，
接着更新prev节点(即将prev节点向前移），
总的来说，反转后的链表是从后往前构建出来的
"""

def reverseList(head):
    pre = None
    while head:
        curr = head
        head = head.next
        curr.next = pre
        pre = cur
    return pre
