"""
扫一遍链表，遇到重复的就跳过，否则继续
"""
def deleteDuplicates(head):
    #边界值情况
    if head == None or head.next == None:
        return head
    #这里把head的值赋给一个新变量p
    #防止listnode到尾部以后，值就变成None了
    #再遍历的话就是None.next，而None没有val，next这些attribute
    #就会报错
    p = head
    while p.next != None:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head
    
