"""
位运算法，用异或运算符
"""
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i
        return result
    
"""
字典法，用字典的get方法返回指定键的值
items方法以列表返回可遍历的元组数组
"""
def singleNumber(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for key, val in dic.items():
        if val == 1:
            return key
