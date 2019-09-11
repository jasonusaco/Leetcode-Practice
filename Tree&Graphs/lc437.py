"""
这题还是标准的dfs，直接递归会占用太多空间，所以我们可以建一个字典
来储存所有从根节点到当前节点的path sum以及他们的frequency
遍历树，在每个节点，我们取得一个当前路劲和，然后如果在这个path之内
有合理的方案，说明一定有一个老路劲和是满足当前路劲和减去老路劲和等于target这个条件的
然后我们只需要把老路径的频率加到result里面就可以
当退出当前层次时候，需要减去当前层次计算出来的和，故每次return之前都有一个减一的动作
时间空间都为O(n)
"""
class Solution(object):
    def pathSum(self, root, target):
        #全局结果和路径
        self.result = 0
        cache = {0:1}

        #递归获取result
        self.dfs(root, target, 0, cache)

        #返回结果
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        #结束条件
        if root is None:
            return
        #计算当前路径和以及老路径和
        currPathSum += root.val
        oldPathSum = currPathSum - target
        #更新结果和路径
        self.result += cache.get(oldPathSUm, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        #dfs 细分
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        #当切换分支的时候，要减去当前层次的pathsum，所以要减1
        cache[currPathSum] -= 1
    
