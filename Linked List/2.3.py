def removeNode(pNode):
    if pNode.next == None:
        return False
    else:
        #如果不是空链表，则把指定节点的下一个节点的值赋给指定节点
        pNode.val = pNode.next.val
        #然后pNode指向再下下个节点
        pNode.next = pNode.next.next
        return True
