"""
每个位置的周长是4，如果该块陆地的左边或者上边
（右边或者下边 或者其他两种随机组合）也是陆地，
则总周长减去2（因为毗邻部分有两条边需要去掉）.
所以整个小岛的周长是4×陆地数-2×相交数
注意不能4个边都减去，因为一个的左边或者上边有，
相当与另一个的右边或者下边有，如果四个都减去的话会重复
"""
class Solution:
    def islandPerimeter(self, grid):
        #储存结果
        result = 0
        #定义长和宽
        height = len(grid)
        if height:
            width = len(grid[0])
        else:
            width = 0
        #遍历二维数组
        for i in range(height):
            for j in range(width):
                #如果坐标是1，那么则是陆地
                #总周长就+4
                if grid[i][j] == 1:
                    result += 4
                    #如果这个点的下边也是1，若有则有一边重复
                    if i > 0 and grid[i-1][j] == 1:
                        result -= 2
                    #左边也是1，也是有一边重复
                    if j > 0 and grid[i][j-1] == 1:
                        result -= 2
        return result
                        
                    
        
