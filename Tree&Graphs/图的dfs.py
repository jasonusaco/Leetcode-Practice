"""
利用栈实现，从源节点开始把节点按照深度放入栈，然后弹出
每弹出一个点，把该节点下一个没有进过栈的邻接结点放入栈
直至栈变空
"""
def dfs(node):
    if node is None:
        return
    nodeSet = set()
    stack = []
    print(node.value)
    nodeSet.add(node)
    stack.append(node)

    while len(stack) > 0:
        #弹出最近入栈的节点
        cur = stack.pop()
        #遍历该节点的邻接结点
        for next in cur.nexts:
            #如果邻接节点不重复
            if next not in nodeSet:
                #把节点压入栈
                stack.append(cur)
                #把邻接节点压入栈
                stack.append(next)
                #登记节点
                set.add(next)
                #打印节点值
                print(next.value)
                #退出，保持深度优先
                break
