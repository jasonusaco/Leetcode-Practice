"""
首先把数据压入stack1，然后出栈到stack2，这个时候
这些数据已经是逆向的存放在stack2里面了，那么如果对
stack2进行出栈，出来的顺序就是这组数据入队的顺序
"""
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    #要入队的时候就把数据压入stackA
    def push(self,node):
        self.stackA.append(node)

    #要出队时，就把stackA里的数据压入stackB，然后对
    #stackB进行出栈就行了
    def pop(self):
        #首先判断stackB是否为空
        if self.stackB == []:
            #如果是的话就把stackA里面元素都pop到stackB里面
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            #然后返回stackB出栈的值就是队列了
            return self.stackB.pop()
        #如果stackB不为空，就直接pop
        return self.stackB.pop()

    
