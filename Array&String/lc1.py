#字典方法,enumerate方法可以同时引出下标和数据
#key是数组的值x，value是相应的位置
#只要满足num和target-x都在字典则找到答案
#时间复杂度为O(n),空间复杂度O(n)
def twoSum(nums,target):
    dic = {}
    for i,x in enumerate(nums):
        y = target - x
        if y in dic:
            return dic[y],i
        dic[x] = i

#双指针法，可以先把数组排序
#然后首尾相加，如果比target大，
#则将尾数左移，如果小了首尾右移，
#直到两个数相加刚好等于target
#zip函数可将里面的两个参数返回成元组
#复杂度为O(nlogn),空间复杂度O(1)
def twoSum(nums, target):
    l = sorted(zip(nums, range(len(nums))))
    left = 0
    right = len(l) - 1
    while left < right:
        v = l[left][0] + l[right][0]
        if v == target:
            return [l[left][1], l[right][1]]
        if v < target:
            left += 1
        else:
            right -= 1
    
    
