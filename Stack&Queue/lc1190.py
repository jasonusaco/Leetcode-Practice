class Solution:
    def reverseParentheses(self, s):
        #括号题想到用栈
        stack = []
        #遍历字符串
        for char in s:
            if char == ')':
                inner_bracket = []
                while True:
                    last = stack.pop()
                    if last == '(':
                        break
                    else:
                        inner_bracket.append(last)
                stack.extend(inner_bracket)
            else:
                stack.append(char)
        return ''.join(stack)
            
