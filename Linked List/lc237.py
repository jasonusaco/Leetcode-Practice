"""
把下一个节点的值赋给当前节点，然后当前节点指向下下个节点，则相当于删除了当前节点
"""
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
