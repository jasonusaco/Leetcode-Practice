"""
挨个比较即可，不满足条件时更新max_len
"""
class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        #计数
        temp = 1
        #这个用于比较
        max_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp += 1
            else:
                max_len = max(max_len, temp)
                temp = 1
        return max(temp, max_len)
