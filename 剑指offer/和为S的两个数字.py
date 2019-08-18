"""
两头匹配，乘积最小的必定为最先找到的
"""
class Solution:
    def FindNumberWithSum(self, array, tsum):
        low = 0
        high = len(array) - 1
        while low < high:
            if array[low] + array[high] > tsum:
                high -= 1
            elif array[low] + array[high] < tsum:
                low += 1
            else:
                return [array[low], array[high]]
        #匹配失败返回空列表
        return []
