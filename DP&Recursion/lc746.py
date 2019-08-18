"""
dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        #初始化全部赋值为0
        step = [0] * (len(cost) + 1)
        i = 2
        #一个数的话直接返回第一个
        if len(cost) == 1:
            return cost[0]
        #两个数的话直接用min取最小的那个
        if len(cost) == 2:
            return min(cost)

        while i <= len(cost):
            step[i] = min(step[i-1]+cost[i-1], step[i-2]+cost[i-2])
            i += 1
        return step[-1]
