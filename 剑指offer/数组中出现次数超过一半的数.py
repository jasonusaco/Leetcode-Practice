"""
记一种比较笨的办法，空间换时间
用字典存每个元素的次数
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dict = {}
        for no in numbers:
            if not dict.has_key(no):
                dict[no] = 1
            else:
                dict[no] = dict[no] + 1
            if dict[no] > len(numbers)/2:
                return no
        return 0
