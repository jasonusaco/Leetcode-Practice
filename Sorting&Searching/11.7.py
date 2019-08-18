"""
动态规划，找出以元素i结尾的最长递增子序列
"""

def getHeight(self, men, n):
    #dp[i]表示已第i个元素结尾的最长递增子序列的长度
    dp = [0] * n
    dp[0] = 1
    #初始化最长子序列的长度
    longest = 0
    for i in range(1, n):
        slgst = 0
        sidx = 0
        while sidx < i:
            if men[sidx] <= men[i]:
                slgst = slgst if slgst > dp[sidx] else dp[sidx]
            sidx += 1
        dp[i] = slgst + 1
        longest = dp[i] if dp[i] > longest else longest
    return longest
    
