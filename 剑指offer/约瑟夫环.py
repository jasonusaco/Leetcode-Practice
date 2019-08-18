"""
约瑟夫环问题：
方法1：使用list模拟循环链表，用cur作为指向list的下标位置。
当cur移到list末尾直接指向list头部，
当删除一个数后list的长度和cur的值相等则cur指向0
"""
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return
        childNum = list(range(n))
        print(childNum)
        cur = 0  # 指向list的指针
        while len(childNum) > 1:
            for i in range(1,m):
                cur += 1
                # 当指针移到list的末尾，则将指针移到list的头
                if cur == len(childNum):
                    cur = 0
            # 删除一个数，此时由于删除之后list的下标随之变化
            # cur指向的便是原数组中的下一个数字，此时cur不需要移动
            childNum.remove(childNum[cur])
            if cur == len(childNum):  # list的长度和cur的值相等则cur指向0
                cur = 0
        return childNum
