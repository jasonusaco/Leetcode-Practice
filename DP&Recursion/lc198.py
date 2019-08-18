"""
第n个房子的最大金额是
f(n) = max(n + nums[n-2], nums[n-1])
就是比较抢当前房子和上上冬房子或者抢前一栋房子哪个多
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0    
        if len(nums) == 1:
            return nums[0]

        #这里建一个dp列表全部列为0
        dp = [0] * len(nums)
        #dp只存最大值，只有一个的时候就返回那个
        #从第二个开始就要比较了
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            #nums[i]代表当前的钱，加上之前的最大值
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        #返回最后一个元素
        return dp[-1]
