class Solution:
    def pivotIndex(self, nums):
        #求出当前数组的综合
        full_sum = sum(nums)
        left = 0
        right = 0
        #len_nums = len(nums)
        for i in range(len(nums)):
            if i > 0:
                left += nums[i-1]
            right = full_sum - left - nums[i]
            if left == right:
                return i
        return -1
