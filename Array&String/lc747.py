class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        maximum = max(nums)
        if len(nums) <= 1:
            return 0
        nums2.pop()
        if nums2[-1]*2 <= maximum:
            return nums.index(maximum)
        return -1
