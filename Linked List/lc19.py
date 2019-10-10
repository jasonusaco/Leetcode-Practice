"""
双指针法，p1先向前移动n个节点，然后p1和p2同时移动
当p1.next == None时，p2.next指的就是需要删除的节点
"""
class Solution:
    def removeNthFromEnd(self, head, n):
        #建立一个新的头结点
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        #p1移动到n
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
        
