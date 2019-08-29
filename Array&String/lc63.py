class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        #如果第一个格子有障碍，就无法前进了
        if obstacleGrid[0][0] == 1:
            return 0
        #纵向
        vertical = len(obstacleGrid)
        #横向
        horizontal = len(obstacleGrid[0])
        dp = [[0 for _ in range(horizontal)] for _ in range(vertical)]

        #第一个可以走设置为1
        dp[0][0] = 1
        #检查第一行和第一列是否有障碍
        for i in range(1, vertical):
            dp[i][0] =  dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, horizontal):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, vertical):
            for j in range(1, horizontal):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[vertical-1][horizontal - 1]
            
