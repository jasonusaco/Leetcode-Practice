"""
垃圾做法：直接计算target一共出现几次，然后获取第一个target的index，
加上出现的次数再减一就是答案了
"""
class Solution:
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        cont = nums.count(target)
        return [nums.index(target), nums.index(target)+cont-1]

"""
看到题目要求要O(logn)，马上想到二分法
"""

class Solution:
    def searchRange(self, nums, target):
        #定义左右指针
        left = 0
        right = len(nums) - 1
        #特殊情况
        if nums == []:
            return [-1,-1]
        #双指针运行条件
        while (left <= right):
            mid = int((left+right)/2)
            if nums[mid] == target:
                #i和j从找到的位置向两边寻找
                i = mid - 1
                j = mid + 1
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j <= len(nums) - 1 and nums[j] == target:
                    j += 1
                return [i+1, j-1]
            #二分法思路，移动左右指针
            if nums[left] <= target and nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]
        
