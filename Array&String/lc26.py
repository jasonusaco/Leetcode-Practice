"""
用i，j两个下标，i记录新数组的下标，j是原来数组下标，
如果nums[j] != nums[j - 1]，那么nums[i] = nums[j]，i 和j 都+ 1。
最后返回i。
"""
def removeDuplicates(nums):
    i = 1
    j = 1
    size = len(nums)
    while j < size:
        if nums[j] == nums[i-1]:
            i += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    return min(i,size)
