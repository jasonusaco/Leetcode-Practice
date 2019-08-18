"""
就是有向图的遍历，可以用dfs，实现起来比较简单，递归+判断节点
是否已经遍历过
"""
class Path:
    def checkPath(self, a, b):
        #set存放已经遍历过得node
        visited = set()
        return self.dfs(a, b,visited) or self.dfs(b, a, visited)
    
    def dfs(self,a,b,visited):
        #如果a和b是同一个node，直接返回True
        if a == b:
            return True
        #遍历该节点的邻接节点
        for i in a.neighbors:
            #只要i不是已经遍历过，就把当前节点加入visited里面
            if i not in visited:
                visited.add(i)
                #递归重复此过程
                return self.dfs(i,b,visited)
        return False
            
