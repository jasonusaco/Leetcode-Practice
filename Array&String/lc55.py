class Solution:
    def canJump(self, nums):
        step = nums[0]
        #从第二个数还是遍历，step每次减一，每次和当前遍历值比较
        #取出最大
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            #如果第一个数小于等于0的话直接false，根本无法前进
            else:
                return False
        return True
