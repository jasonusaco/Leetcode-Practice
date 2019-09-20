from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)+1):
            nums.append(i)
        nums1 = dict(Counter(nums))
        for i in nums1:
            if nums1[i] == 3:
                res.append(i)
            if nums1[i] == 1:
                res.append(i)
        return res
