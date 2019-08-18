"""
新建一个链表，next用两个链表当前位置去比较，谁的小就放谁。
当一个链表放完之后，说明另外一个链表剩下的元素都比较大，再放进去就好。
复杂度O(m+n)
"""
def mergeTwoLists(l1,l2):
    #先判断是否在两个链表中
    if not l1 and not l2:
        return None
    #创建新链表用于添加比较完大小的元素
    result = ListNode(0)
    l = result
    while l1 and l2:
        if l1.val < l2.val:
            l.next = l1
            l1 = l1.next
        else:
            l.next = l2
            l2 = l2.next
        #融合后链表的下一位，当前位置刚刚赋值
        l = l.next
    #把剩余的链表排在后面
    l.next = l1 or l2
    #融合后链表从第二个对象开始返回，第一个对象是自己创建的ListNode(0)
    return result.next
    
