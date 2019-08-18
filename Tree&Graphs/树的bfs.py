def bfs(node):
    if node is None:
        return
    queue = []
    queue.insert(0,node)
    while queue:
        #弹出元素
        cur = queue.pop()
        #打印元素值
        print(cur.val)
        #遍历元素邻接节点
        for next in cur.nexts:
            #直接加入并登记
            queue.insert(0,next)
