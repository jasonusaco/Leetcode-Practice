"""
动态规划，子问题
一个数的数组最大子段和：dp[0] = nums[0]
两个数的数组最大子段和:两种情况，加上第一个数或不加第一个数
加上第一个:dp[0]+nums[1]
不加：nums[1]
dp[1] = max(dp[0] + nums[1], nums[1])
然后再取max(dp[0], dp[1])
所以n个数的数组的最大子段和：dp[n-1] = (dp[n-2]+nums[n-1], nums[n-1])
max(dp[0], dp[1],...dp[n-1])
"""
class Solution(object):
    def maxSubArray(self, nums):
        dp = []
        if len(nums) == 0:
            return []
        #dp[0] = nums[0]
        dp.append(nums[0])
        #起始最大值定位最后一个
        max_dp = dp[-1]
        #开始在列表里遍历
        for i in range(1, len(nums)):
            #遍历的时候就把n个数的数组的最大子段和加到dp里
            dp.append(max(dp[i-1] + num[i], nums[i]))
            #只要当前最大值没有dp中最后一位大
            #就把最后一位的值赋给当前最大
            if max_dp < dp[-1]:
                max_dp = dp[-1]
        return max_dp
