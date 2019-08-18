"""
方法1:递归，每次将左子树结果和右子树结果存到结果集中
"""
class Solution:
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        #结果集
        ans = []
        ans.append(root.val)
        self.orderans(root, ans)
        return ans

    def orderans(self, root, ans):
        if not root:
            return
        if root.left:
            ans.append(root.left.val)
        if root.right:
            ans.append(root.right.val)

        self.orderans(root.left, ans)
        self.orderans(root.right, ans)

"""
方法2：BFS，借助队列，先把根节点加入队列
每次从队列头取出一个节点，访问
然后把它的左右子节点加入队列尾部，重复此过程
直到队列为空
"""

class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        #把根节点入队
        queue = [root, ]
        output = []
        while(queue):
            #从队列头取出头节点访问
            output.append(queue[0].val)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
        return output
