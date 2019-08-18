"""
方法1：递归
1、递归出来的条件就是递归到的次数等于输入串的长度
if num == length:
res.append(string)
return
2、这里要循环进入递归，可以设置断点调试很容易理解
for c in ying_se[digits[num]]:
dfs(num + 1, string + c, res)
3、当输入的串长为0，即’'这种情况直接返回空列表。if length == 0: return []
"""
class Solution(object):
    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            else:
                for c in ying_se(digits[num]]:
                    dfs(num+1, string+c, res)
        ying_se = {'2': 'abc', '3': 'def', '4': 'ghi',
                   '5': 'jkl', '6': 'mno', '7': 'pqrs',
                   '8': 'tuv', '9': 'wxyz'}
        length = len(digits)
        if length == 0:
            return []
        res = []
        dfs(0, '', res)
        return res
