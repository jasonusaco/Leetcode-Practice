"""
本题是标准的DP问题，可以看到很明显的子结构
首先是top-down的思考方式，如果要爬到n台阶，就只有两种可能性
1.在n-1的台阶处爬一层台阶
2.在n-2的台阶处爬两层台阶
那么再往下，达到每一层一共有几种方法，这个问题就变成了2个子问题
1.到达n-1层台阶有几种方法
2.到达n-2层台阶有几种方法
最后取返回子问题之和即可
"""

#根据思路，我们可以写出最简单的递归代码
#这种方法会timeout，因为随着计算次数的增多，复杂度会呈指数级增长
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

#那么，如果要优化的话，可以考虑将之前已经计算好的结果保存起来，
#之后如果遇到重复计算就直接调用，这样复杂度会从之前的指数级变成O(n)
#实现方法是简历一个长度为N的列表，将里面的值全部赋值为-1，因为这类问题
#基本不会让你去求负数种的可能性，所以-1可以成为一个很好的递归出口
class Solution Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        res = [-1 for i in range(n)]
        res[0] = 1
        res[1] = 2
        return self.dp(n-1, res)
    
    def dp(self, n, res):
        if res[n] == -1:
            res[n] = self.dp(n-1, res) + self.dp(n-2, res)
        return res[n]
    
"""
接下来考虑Bottom-Up的思考方式，在每一层，我们只需要知道在当前节点，我们的n-1
和n-2的值是多少即可
"""
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
