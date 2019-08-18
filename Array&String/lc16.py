"""
先给数组排序，这里复杂度为O(nlogn),
然后使用一个指针遍历这里的复杂度为O(n)，另
外两个指针分别指向下一个元素和最后一个元素
然后向中间靠拢的方式，如果当前的和与target的差距
比要返回的结果与target更小，那么更新要返回的结果,这里也是O(n)
指针移动策略是如果比目标值大，说明我们需要把这个和调小一点，反之亦然
如果相等那么就返回结果
合起来复杂度为O(n^2)
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        res = float('inf')
        #遍历排序后的数组，t是第一个数
        for t in range(n):
            #i为下一个元素，j为最后一个元素
            i, j = t+1, n-1
            #指针进行条件，两个指针还没碰面
            while i < j:
                #三个数的sum
                sums = nums[t] + nums[i] + nums[j]
                #用三数和与target进行比较，如果一样直接返回
                if abs(sums-target) < abs(res-target):
                    res = sums
                #如果更大，则尾部指针向做移动
                if sums > target:
                    j -= 1
                #如果更小，头部指针向右移动
                elif sums < target:
                    i += 1
                else:
                    return target
        return res
