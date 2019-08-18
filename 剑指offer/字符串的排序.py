class Solution:
    def __init__(self):
        self.result = []
    def Permutation(self, ss):
        if not ss:
            return []
        # python 不可直接修改string，先变成char数组
        chars = list(ss)
        # 开始递归
        self.permute(chars, 0)
        # 最终结果去重、排序
        res = list(set(self.result))
        res.sort()
        return res
    def permute(self, string, begin):、
        # 已经递归到底了
        if begin == len(string):
            self.result.append(''.join(string))
        else:
            # 轮番从各个位置的char中选一个当作首位，交换位置
            for i in range(begin, len(string)):
                string[i], string[begin] = string[begin], string[i]
                # 固定首位，递归余下的
                self.permute(string, begin+1)
                # 记得换回去
                string[i], string[begin] = string[begin], string[i]
