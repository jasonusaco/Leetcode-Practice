"""
可以用递归
递归结束条件，节点是None，结束函数调用
递归改变：每次都要把节点添加到节点集合当中去
递归调用：对于每一个当前节点的相邻节点，只要不在节点集合中，就调用dfs进行搜索
"""
def dfs(node):
    if node is None:
        return
    print(node.val)
    for next in node.nexts:
        dfs(next)

