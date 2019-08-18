"""
看到最短路径首先想到bfs，利用队列来存放节点
字典存放(0,0)到该节点的距离，洪水可以从四个方向流进来
也就是说可以从所有的邻节点到达
要有一个获取邻节点的函数用于避开有建筑的点
"""
class Flood:
    def floodFill(self, tmap, n, m):
        self.m = m
        self.n = n
        self.tmap = tmap
        #创建队列和字典并定义初始位置
        queue = []
        distance = {}
        distance[(0,0)] = 0
        while queue:
            pop_point = queue.pop()
            for point self.graph_Neighbor(pop_point):
                if point not in distance:
                    queue.append(point)
                    distance[point] = distance[pop_point]+1
        return m+n-2

    #用于获取邻节点
    def graph_Neighbor(self, p):
        neighbor = []
        i = p[0]
        j = p[1]
        #四个角的边界情况
        if 0 <= i-1 and self.tmap[i-1, j] == 0:
            neighbor.append((i-1, j))
        if 0<=i+1<n and self.tmap[i+1, j]==0:
            neighbor.append((i+1, j))
        if 0<=j-1<n and self.tmap[i, j-1]==0:
            neighbor.append((i, j-1))
        if 0<=j+1<n and self.tmap[i, j+1]==0:
            neighbor.append((i, j+1))
        return neighbor
