"""
额外定义一个辅助栈stack，把数据从pushV
中压，如果压入数据和popV出栈元素一致，
就从pushV和popV中同时弹出去，不往stack中压了
等到pushV中元素全部弹出来以后，判断stack中出栈元素和
popV中出栈元素是否一致，当popV中元素全部弹出，就结束
如果最后辅助栈不为空说明弹出序列不是该栈的弹出序列
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        push_cursor = 0
        for pop in popV:
            if stack and pop == stack:
                stack.pop()
            else:
                while not(stack and pop == stack[-1]) and push_cursor < len(pushV):
                    stack.append(pushV[push_cursor])
                    push_cursor += 1
                if push_cursor == len(pushV) and stack[-1] != pop:
                    return False
                else:
                    stack.pop()
        return True
