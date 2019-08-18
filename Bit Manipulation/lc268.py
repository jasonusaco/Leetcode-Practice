"""
方法1：等差数列求和公式
求出前n项和，以此减去list中的元素
最后差值就是没出现过的元素
公式为Sn = na1+n(n-1)d/2,其中a1为首项，an为末项
n为项数，公差为d，Sn是前n项的和
"""
class Solution:
    def missingNumber(self, nums):
        #n为项数
        n = len(nums)
        #求和公式
        b = int(n*(n+1)/2)
        #当前给定的数组的和
        sums = sum(nums)
        #差即是答案
        return b - sums

"""
方法2：先把数组排序，然后返回第一个与自然数组元素不相等的元素

"""
class Solution:
    def missingNumber(self, nums):
        i = 0
        nums.sort()
        #如果item - i不等于0了，说明跳了，就返回这个数
        for item in nums:
            if item - i != 0:
                return i
            else:
                i += 1
        return i
