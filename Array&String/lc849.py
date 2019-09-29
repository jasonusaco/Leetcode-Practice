class Solution:
    def maxDistToClosest(self, seats):
        left = -1
        count = 0
        ans = 0
        for i, val in enumerate(seats):
            #先计算0的数量
            if val == 0:
                count += 1
            else:
                #如果左边没人的话
                if left == -1:
                    distance = count
                #如果左右各有一个人
                else:
                    distance = (count+1)//2
                #更新左指针
                left = i
                count = 0
                ans = max(ans, distance)

        return max(ans, count)
