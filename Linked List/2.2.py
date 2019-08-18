"""
创建一个新列表，当头结点不是空时，依次把头节点加入到新列表
如果k的值没有超出新列表的范围，返回None
正常返回-k就可以得到倒数k个结点
"""
def FindKthToTail(head,k):
    l = []
    while head != None:
        l.append(head)
        head = head.next
    if k > len(l) or k < 1:
        return None
    return l[-k]

"""
快慢针法，两个指针，都先指向头结点，
然后让第一个指针走k-1步；到达第k个节点，
然后两个指针同时往后移，当第一个节点到达末尾的时候，
第二个节点所在位置就是倒数第k个节点了
"""
def FindKthToTail(head,k):
    fast = head
    slow = head

    #在范围里面遍历，让fast到达k-1的位置，就是第k个元素
    for i in range(k):
        if fast == None:
            return None
        if fast.next == None and i == k-1:
            return head
    #这时两个指针同时动，只要快针的下一个节点没到头，就继续
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    #最后返回慢指针
    return slow.next
