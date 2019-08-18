class Stack(object):
    def __init__(self):
        self.stack = []

    #进栈
    def push(self,value):
        self.stack.append(value)

    #出栈
    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise LookupError("stack is empty")

    #栈为空
    def is_empty(self):
        return bool(self.stack)

    #取出目前stack中的最新元素，最顶上的元素
    def peek(self):
        return self.stack[-1]
