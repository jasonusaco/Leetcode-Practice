"""
使用栈，遇到左括号就放到栈里面，遇到右括号
就先判断栈里有没有左括号，有的话就弹出一个
没有的话直接false
最后判断这个栈是否为空
"""class Parenthesis:
    def chkParenthesis(self, A, n):
        stack = []
        for i in A:
            if i == "(":
                stack.append("(")
            elif i = ")":
                #检查栈里面是否有左括号
                if not stack:
                    return False
                stack.pop()
        return stack==[]
