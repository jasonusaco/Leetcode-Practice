"""
核心思想是用双指针解决2sum问题然后再递归解决nsum
"""
def fourSum(self, nums, target):
    def findNsum(nums, target, N, result, results):
        #特殊情况，如果数量小于2,
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
            return
        #two sum方式，双指针
        if N == 2:
            left = 0
            right = len(nums)-1
            #双指针的结束条件
            while left < right:
                #计算和
                sums = nums[left] + nums[right]
                if sums == target:
                    results.append(result, [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif sums < target:
                    left += 1
                else:
                    right -= 1
        #N-sum
        else:
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results
