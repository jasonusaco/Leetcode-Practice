"""
数组内部求满足要求的subarray，滑动窗口思想
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        sum = 0
        maxsum = None
        for i in range(len(nums)):
            sum += nums[i]
            if i >= k:
                sum -= nums[i-k]
            if i >= k-1:
                maxsum = max(sum/k, maxsum)
        return maxsum

class Solution(object):
    def findMaxAverage(self, nums, k):
        #先求出最开始的k个数字的和
        last_sum = sum(nums[0:k])
        max_sum = last_sum
        #从第k个数字开始遍历
        for i in range(len(nums)-k):
            #前k位加上第k+1位再减去第一位，如此往复
            last_sum = last_sum + nums[i+k]-nums[i]
            #对比前k个的和以及后面每k个的和谁大
            max_sum = max(max_sum, last_sum)
        #最后取平均数
        return max_sum/float(k)
