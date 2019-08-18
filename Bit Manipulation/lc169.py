"""
依然可以用字典，因为字典可以用item返回可遍历元组
同时可以统计数量
"""
class Solution(object):
    def majorityElement(self, nums):
        import collections
        key_dict = {}
        key_dict = collections.Counter(nums)
        for key, values in key_dict.items():
            if values > len(nums)/2:
                return key
