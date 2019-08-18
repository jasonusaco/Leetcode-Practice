"""
链表A和链表B的长度可能不相等, 所以我们需要将较长的链表多出的节点忽略掉
将较长的链表的head移动n次, n为多出的长度. 然后同时遍历链表A和链表B,
当headA == headB时, 返回节点.这里的edge case是两个链表都只有1个节点且在头部重合,
因此判断重合的条件必须是headA == headB, 而不是headA.next == headB.next
Time: O(m) + O(n) + O(max(m, n)), m, n分别是链表的长度
Space: O(1)

"""
def getIntersectionNode(headA, headB):

    #用于表示两个链表的长度并初始化
    len1 = 0
    len2 = 0

    #赋值给两个新变量用于遍历
    moveA = headA
    moveB = headB

    #分别获取两个链表的长度并赋值到len1和len2
    while moveA:
        len1 += 1
        moveA = moveA.next

    while moveB:
        len2 += 1
        moveB = moveB.next

    #如果l2更长的话，遍历范围就是两个链表的长度差
    if len1 < len2:
        for i in range(len2 - len1):
            headB = headB.next
    else:
        for i in range(len1 - len2):
            headA = headA.next
    while headA and headB and headA != headB:
        headA = headA.next
        headB = headB.next
    return headA

def getIntersectionNode(self, headA, headB):
    len1 = self.getLength(headA)
    len2 = self.getLength(headB)

    if len1 > len2:
        for i in range(len1 - len2):
            headA = headA.next
    else:
        for i in range(len2-len1):
            headB = headB.next

    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

def getLength(self, head):
    l= 0
    while head:
        l += 1
        head = head.next
    return l
