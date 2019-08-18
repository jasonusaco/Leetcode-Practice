"""
dp[j]表示可以使用的硬币方法
dp[j-coins[i]]表示使用一个coins[i]拼接成j的方法
同时，由于按硬币面值从小到大考虑，dp[j]为前i种类型硬币
进行组合时的组合数，当组成j的币值种类中包含coins[i]时，
计算如下：
组成面值和为j的硬币中，最后一枚不使用coins[i]时的组合数，即上一步所求结果dp[j]
组成面值和为j的硬币中，最后一枚使用coins[i]时的组合数,即dp[j-coins[i]]
这两个事件构成了事件的全体，因此dp[j] = dp[j]+dp[j-coins[i]]
"""
class Coins:
    def countWays(self, n):
        coins = [1, 5, 10, 25]
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
         
        for i in range(4):
            for j in range(coins[i], n + 1):
                dp[j] = (dp[j] + dp[j - coins[i]]) % 1000000007
        return dp[n]
        
