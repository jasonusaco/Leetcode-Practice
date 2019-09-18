class Solution(object):
    def matrixReshape(self, nums, r, c):
        width = len(nums)
        height = len(nums[0])
        if width * height != r*c:
            return nums
        res = []
        row = []
        for i in range(width):
            for j in range(height):
                #遍历过程中使用可变的list作为新的一行
                row.append(nums[i][j])
                #如果新的一行的元素个数等于题目要求的列数，
                #那么就新建一行。把每行的结果放到返回的列表中即可
                if len(row) == c:
                    res.append(row)
                    row = []
        return res
