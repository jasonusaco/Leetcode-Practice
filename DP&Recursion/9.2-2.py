"""
动态规划，dp[i][j]表示起点到(i,j)有多少条路径
起点到(i,j)的路径等于起点到(i-1,j)的路径加上起点到(i,j-1)的路径
即dp[i][j] = dp[i-1][j] + dp[i][j-1]
"""
class Robot:
    def countWays(self, m, x, y):
        if not m or len(m) != x or len(m[0]) != y:
            return 0
        if m[x-1][y-1] != 1 or m[0][0] != 1:
            return 0

        dp = [[0] * y for i in range(x)]
        dp = [0][0] = 1

        for i in range(1,x):
            if m[i][0] == 1:
                dp[i][0] = dp[i-1][0]
        for j in range(1,y):
            if m[0][j] == 1:
                dp[0][j] = dp[0][j-1]

        for i in range(1,x):
            for j in range(1,y):
                if m[i][j] == 1:
                    dp[i][j] = dp[i-1][j] % 1000000007 + dp[i][j - 1] % 1000000007
        return dp[x-1][y-1] % 1000000007
        
                    
