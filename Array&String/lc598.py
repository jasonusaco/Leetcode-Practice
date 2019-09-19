"""
最终二维数组中最大值出现的次数一定是操作中最小范围中的那批元素构成的矩形区域面积。
"""
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        #如果没有进行任何操作，应该返回全部0的个数
        if not ops:
            return m * n
        return min([op[0] for op in ops]) * min([op[1] for op in ops])
