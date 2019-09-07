class Solution:
    def thirdMax(self, nums):
        nums_set = set(nums)
        if len(nums_set) < 3:
            return max(nums_set)
        return sorted(nums_set)[-3]
