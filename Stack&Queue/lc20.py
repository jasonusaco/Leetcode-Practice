"""
用栈来操作，将所有字符依次入栈，当栈顶的括号和整要入栈的括号匹配时，
将栈顶的括号弹出且不入栈，否则入栈新的括号，只有当栈为空时才表明输入有效
"""
class Solution:
    def isValid(self, s):
        #开一个空栈
        stack = [None]
        
        #建一个字典来存放三种对应括号
        parmap = {')': '(', '}': '{', ']': '['}
        
        #在给定string里面遍历
        for c in s:
            #首先确定是否为6个括号元素之一
            if c in parmap:
                #如果是其中之一则判断当前字符是否和栈里面弹出的是对应关系
                #若不是，则返回false
                if parmap[c] != stack.pop():
                    return False
            #如果c不在6个括号元素里，就把c加入到栈当中
            else:
                stack.append(c)
        return len(stack) == 1
