"""
双层遍历，找出为0的坐标对，然后存放到一个set里面
"""
class Solution:
    def setZeroes(self, matrix):
        row = len(matrix)
        column = len(matrix[0])

        hash_set = set()

        for i in range(row):
            for j in range(column):
                hast_set.add((i,j))

        for pair in hash_set:
            r = pair[0]
            c = pair[1]
            matrix[r] = [0]*column
            for i in range(row):
                matrix[i][c] = 0
