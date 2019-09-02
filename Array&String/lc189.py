"""
思路1，开辟新内存，将后面k个元素先存起来，然后将原数组中从第一个
到第n-k个，都往后移动k位，最后再将先前保存的k位放在原数组前面即可
"""
class Solution:
    def rotate(self, nums, k):
        extra = nums[-k:]
        return extra+nums[0:-k]
        
        
"""
思路2:经典反转法，先把前n-k个元素reverse
然后把剩下的reverse，最后把整个列表一起reverse
"""

class Solution:
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
