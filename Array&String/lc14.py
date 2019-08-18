"""
首先考虑两种边界情况

字符串数组为空，则最终输出一个空字符串
字符串数组中只有一个字符串时，直接输出该字符串即可

思路：二分查找，以数组中的最短元素来作为比较基准，然后
用基准元素的前一半进行比较
"""

def longestCommonPrefix(strs):
    #特殊情况处理
    if len(strs) < 1:
        return ""
    if len(strs) == 1:
        return strs[0]

    minElement = strs[0]
    #这里是遍历获取数组中的最短元素
    for i in range(len(strs)):
        if len(str[i]) < len(minElement):
            minElement = strs[i]
            
    #二分法实现
    left = 0
    right = len(minElement)
    mid = (left+right) // 2
    while left < right:
        flag = True
        for j in range(len(strs)):
            #不符合前缀停止条件
            if minElement[:mid+1] != strs[j][:mid+1]:
                right = mid
                flag = False
                break
        if flag:
            left = mid+1
        mid = (left+right) // 2

    #遍历结束后，mid位置就是截取的停止下一位置
    return minElement[:mid]
