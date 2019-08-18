"""
双指针法，一个指向当前处理好的链表
另一个指向正在处理的节点
"""
class Solution:
    def deleteDuplication(self, pHead):
        #如果是空链表或者只有一个元素的链表
        #直接返回
        if not pHead or not pHead.next:
            return pHead

        #构造一个新头结点
        head = ListNode(0)
        head.next = pHead
        pre = head
        last = head.next
        while last:
            #当前节点有next并且和他的next的val相同
            #说明这一串都要被抛弃
            if last.next and last.val == last.next.val:
                while last.next and last.val == last.next.val:
                    last = last.next
                pre.next = last.next
                last = last.next
            else:
                #如果当前节点没有next
                #或者和他的next val不同，则将此节点
                #接入链表，并且继续往后走
                pre = pre.next
                last = last.next
        return head.next
