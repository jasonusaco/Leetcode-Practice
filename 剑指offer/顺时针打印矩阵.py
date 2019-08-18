"""
一圈一圈打印，难点在于边界条件
一共分四步走，首先第一步总会执行，
行数多于1才会走第二步
行数多余1且列数多于1才会走第三步
行数多于2且列数多于1
"""
class Solution:
    def printMatrix(self, matrix):
        #给的是二维列表，要返回列表
        if not matrix:
            return matrix
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        start = 0

        #先判断是否继续往里走一圈
        while cols > start * 2 and rows > start * 2:
            #走一圈代码
            end_x = cols - 1 - start
            end_y = rows - 1 - start

            #打印第一行
            for i in range(start, end_x+1):
                result.append(matrix[start][i])

            #打印最后一列
            if start < end_y:
                for i in range(start+1, end_y+1):
                    result.append(matrix[i][end_x])

            #打印最后一行
            if start < end_x and start < end_y:
                for i in range(end_x-1, start-1, -1):
                    result.append(matrix[end_y][i])

            #打印第一列
            if start < end_x and start < end_y - 1:
                for i in range(end_y-1, start, -1):
                    result.append(matrix[i][start])
            start += 1
        return result
