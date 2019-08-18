"""
类似bfs搜索二叉树，遍历到depth层时，以及遍历了depth-1了
这个时候只要记住到哪一层了就可以了，借助队列实现bfs，遍历到
depth层是连接链表并结束遍历
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def getTreeLevel(self, root, dep):
    if not root:
        return None

    queue = []
    queue.append((1, root))
    head = p = ListNode(-1)

    while queue:
        top = queue.pop(0)
        if top[0] == dep:
            node = ListNode(top[1].val)
            p.next = node
            p = p.next
        else:
            if top[1].left:
                queue.append((top[0] + 1, top[1].left))
            if top[1].right:
                queue.append((top[0] + 1, top[1].right))
    return head.next
