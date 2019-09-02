"""
用字典，遍历所有元素，将元素值当做键，元素下标当做值
存放在一个字典中，遍历的时候，如果发现重复元素，则比较其下标的差值是否小于k
如果小于则可直接返回true，否则更新字典中该键的值为新的下标
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        t = {}
        for i in range(len(nums)):
            if(nums[i] in t and i-t[nums[i]]<=k):
                return True
            else:
                t[nums[i]] = i
        return False
        
