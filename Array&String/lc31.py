class Solution:
    def nextPermutation(self, nums):
        #length记录数组长度，l用来循环
        length = l = len(nums)
        #记录是否进入循环，如果没有正面是最大的直接反序
        flag = True
        while(l >= 2):
            #倒序寻找一个前一个小于后一个的位置，用于交换
            if nums[l-1] > nums[l-2]:
                flag = False
                left = l-2
                right = -1
                #寻找一个刚好大于我们要交换的数
                for i in range(l-1, length):
                    if nums[l-2] >= nums[i]:
                        right = i - 1
                        break
                #交换
                nums[left], nums[right] = nums[right], nums[left]
                #后半段反序
                nums[left+1: length] = list(reversed(nums[left+1: length]))
                break
            l -= 1
        #如果没有进入循环正面是最大的，直接反序
        if flag:
            nums.reverse()
