"""
遍历所有节点，同时保留每个节点的上一个节点，当遇到节点值是val时，删除该节点。
为了方便操作，定义了一个伪头节点。
"""
def removeElements(self, head, val):
    #定义一个新的伪头结点和上一个节点
    new_head = pre = ListNode(0)
    #赋值给pre.next
    pre.next = head
    while head:
        if head.val == val:
            #如果发现了要删除的目标值，就把头结点的下一个值赋给上一个节点的
            #下一个值，这样相当于head就被删掉了
            pre.next = head.next
        else:
            pre = pre.next
        head = head.next
    return new_head.next
    
