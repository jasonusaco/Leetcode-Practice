"""
一个单链表如果不存在环，则最后一个元素的下一个节点必然为null.
设置两个指针，一个慢指针和一个快指针。将链表的环想象成是一个圆形操场，
两个人在同一起跑线开始绕着操场无限循环跑，那么快的人必然会再一次和慢的人相遇，
即快指针的元素和慢指针的元素相同时，即说明存在环。 

"""
def hasCycle(head):
    if head. == None:
        return False
    #快慢针都要先把head的值赋给他们
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

"""
方法2，采用异常
"""
def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
    
