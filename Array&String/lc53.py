"""
算法时间复杂度为O(n)，一次遍历数组，对数组进行累加的操作。

需要维护两个变量，分别为局部最优curr_sum，和全局最优max_sum。

遍历数组时，从第一个元素开始累加，并赋值给局部最优curr_sum，
当局部最优为负数时，可放弃对应子串，重置局部最优为0。

每一次计算出新的局部最优时，与当前全局最优比较，将较大的值付给全局最优。

最后通过一次遍历，找到子串的最大和。

"""

def maxSubArray(nums):
    curr_sum = 0
    max_sum = -10000000
    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum
