"""
利用队列实现，从源节点开始依次按照宽度进队列，然后弹出
没弹出一个节点，就把该节点所有没进入队列的邻节点放入队列
知道队列变空
"""
from queue import Queue
def bfs(node):
    if node is None:
        return
    queue = Queue()
    nodeSet = set()
    #put方法用于往队列里放数据
    queue.put(node)
    nodeSet.add(node)
    #如果队列不为空，返回True,反之False 
    while not queue.empty():
        #弹出元素
        cur = queue.get()
        #打印元素值
        print(cur.val)
        #遍历元素的邻接节点
        for next in cur.nexts:
            #如果邻接节点没入过队，则加入队并登记
            if next not in nodeSet:
                nodeSet.add(next)
                queue.put(next)
