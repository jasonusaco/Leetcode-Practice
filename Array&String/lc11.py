"""
暴力解的话时间是O(n^2)，会超时
可以使用双指针，一个从最左边一个从最右边，比较两个挡板
矮的就向中间移动，这样每次都保留了比较长的挡板
如果两个高度一致，则移动任意一个，如果移动中遇到更高的挡板，那么
当前挡板决定了以后挡板的最低值，保留遍历过程中的最大值，返回即可
"""
class Solution(object):
    def maxArea(self, height):
        ans = 0
        #左指针
        left = 0
        #右指针
        right = len(height) -1
        #指针结束条件
        while left < right:
            #面积计算
            ans = max(ans, min(height[left], height[right])*(right-left))
            #小的那个移动，左指针往右，右指针往左
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
        
