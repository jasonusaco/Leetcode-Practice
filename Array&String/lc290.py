"""
首先把str转成由单词组成的列表，然后和pattern比较长度
如果不一样直接false，然后定义两个dict
一个储存pattern中各字母出现的下标
另一个储存str中各单词出现的下标
key是字母或单词，value是下标
再通过循环比较字符串中重复出现的下标是否相同
"""
class Solution:
    def wordPattern(self, pattern, str):
        #用空格区分，x为列表
        x = str.split(' ')
        if len(pattern) != len(x):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(x)):
            if pattern[i] in dict1:
                dict1[pattern[i]].append(i)
            else:
                dict1[pattern[i]] = [i]
            if x[i] in dict2:
                dict2[x[i]].append(i)
            else:
                dict2[x[i]] = [i]
            if dict1[pattern[i]] != dict2[x[i]]:
                return False
        return True
            
