"""
matrix[i][j],i是横坐标，j是纵坐标,先以左上角为头的对角线对折一次，
然后再把横坐标反转一次即可
矩阵反转的通用做法，如果是顺时针转，则先上下反转然后对角线对折
如果是逆时针转，则先左右翻转，然后对角线对折
"""
class Solution(object):
    def rotate(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        
