class Solution:
    def findUnsortedSubarray(self, nums):
        sort = sorted(nums)
        res = []
        for i in range(len(nus)):
            if nums[i] != sort[i]:
                res.append(i)
        if not res:
            return 0
        else:
            return res[-1]-res[0]+1
