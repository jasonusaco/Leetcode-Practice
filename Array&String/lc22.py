class Solution:
    def generateParenthesis(self, n):
        res = []
        #res代表返回用的结果列表
        #string是当前括号匹配字符串
        #n是括号对数
        #left是左括号数，right是右括号数
        def dfs(res, string, n, left, right):
            #左括号数等于括号对数时，只需加入剩余右括号，当前匹配字符串括号匹配结束，加入res
            if left == n:
                for i in range(right, n):
                    string += ')'
                res.append(string)
                return
            #左括号等于右括号或者当前一个括号也没有时，只能加入左括号，并把左括号数+1
            elif left == right or left == 0:
                string += '('
                dfs(res, string, n, left+1, right)
            #其他情况既能加入左括号也可以加入右括号，切把相应符号数+1
            else:
                dfs(res, string + ')', n, left, right+1)
                dfs(res, string + '(', n, left+1, right)
        dfs(res, '', n, 0,0)
        return res
                
        
