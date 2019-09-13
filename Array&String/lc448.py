"""
直接用set，然后遍历元列表，不在set里面的取出来即可
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        numset = set(nums)
        for i in range(1, len(nums)+1):
            if i not in numset:
                res.append(i)
        return res
