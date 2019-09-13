"""
遍历points，对每一个点，构建一个字典，字典的key是它与其他店的距离
value是距离的计数，计算距离之后，我们遍历字典，求出这个point
对应所有的boomerang的个数，用排列组合计算
时间复杂度:O(n^2)
空间:O(n)
"""
class Solution:
    def numberOfBoomerangs(self, points):
        #储存答案
        res = 0
        #遍历每个点
        for x in points:
            #构建字典
            count = {}
            for y in points:
                #点与点的距离公式
                d = (x[0]-y[0])**2 + (x[1]-y[1])**2
                #字典中获取每个key对应的value
                count[d] = count.get(d,0) + 1
            for d in count:
                #排列组合法计算总数
                res += count[d]*(count[d]-1)
        return res
