"""
可以创建两个链表，一个链表是存放小于x的元素，
另一个链表存放大于等于x的元素，然后遍历一遍原有链表，
将小于x元素的节点加到第一个链表上，将大于等于x元素的节点加到第二个链表上。
便可实现分割
"""
def partition(pHead, x):
    smallHead = ListNode(0)
    bigHead = ListNode(0)
    small = smallHead
    big = bigHead
    while pHead is not None:
        if pHead.val < x:
            small.next = pHead
            small = small.next
        else:
            big.next = pHead
            big = big.next
        pHead = pHead.next

    big.next = None
    small.next = bigHead.next
    return smallHead.next
    
