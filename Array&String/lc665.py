class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) < 2:
            return True
        #设置计数器
        count = 0
        #遍历nums
        for i in range(1, len(nums)):
            #如果前一个比后一个小，说明是递增
            if nums[i-1] > nums[i]:
                count += 1
                #这种情况就改小
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                #否则改大
                else:
                    nums[i] = nums[i-1]
                #只要改动超过1次则false
                if count > 1:
                    return False
        return True
        
