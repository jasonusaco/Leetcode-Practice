"""
思路1：看成组合问题，一共要走m-1次向下，n-1次向右，两者加起来
也就是说一共要在n+m-2中选出m-1次向下，也就是m+n-2Cm-1
"""
class Solution:
    def uniquePaths(self, m, n):
        ans = 1
        temp = 1
        m -= 1
        n -= 1
        t = min(m,n)
        i = 0
        while i < t:
            ans *= (m+n-i)
            temp *= (t-i)
            i += 1
        return ans/temp

"""
思路2:DP,由于只能向下走，所以从[1][1]开始的格子需要选择走法
"""

class Solution(object):
    def uniquePaths(self, m, n):
        #画出dp的grid
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, n):
            for j in range(1,m):
                #每一个怎么走
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[m-1][n-1]
