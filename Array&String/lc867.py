class Solution:
    def transpose(self, A):
        #先确定长和宽
        row = len(A)
        column = len(A[0])
        #新建一个行数等于原始列数行数的矩阵
        res = [[0] * row for _ in range(column)]
        #对原矩阵进行遍历
        for rows in range(row):
            for col in range(column):
                #然后吧原矩阵倒过来加入到新矩阵
                res[col][rows] = A[rows][col]
        #返回新矩阵
        return res
