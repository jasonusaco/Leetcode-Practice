"""
用栈来操作，将所有的字符依次入栈，
当栈顶的括号和正要入栈的括号匹配时将栈顶的括号弹出且不入栈，否则入栈新的括号。
最后，只有当栈里没有括号时，才表明输入是有效的。
"""
def isValid(s):
    pars = [None]
    parmap = {')':'(','}','{',']','['}
    for c in s:
        if c in parmap and parmap[c] == pars[len(pars)-1]:
            pars.pop()
        else:
            pars.append(c)
    return len(pars) == 1
