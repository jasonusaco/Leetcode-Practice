"""
BFS遍历，用队列，遍历完直接求平均值
"""
import collections
class Solution(object):
    def averageOfLevel(self, root):
        #定义队列
        queue = collections.deque()
        #res用于存放答案
        res = []
        #bfs顺序是从root开始依次按照宽度进入队列，然后弹出
        queue.append(root)
        while queue:
            size = len(queue)
            #保存每一行
            row = []
            for _ in range(size):
                #把队列头元素加入到node中
                node = queue.popleft()
                if not node:
                    continue
                #把node的值加入到行的列表中
                row.append(node.val)
                #持续把左右子树的节点加入到队列中
                queue.append(node.left)
                queue.append(node.right)
            #在每一行中求平均数
            if row:
                res.append(sum(row) / float(len(row)))
        return res
