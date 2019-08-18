class Solution:
    def __init__(self):
        self.num = []
        
    def push(self, node):
        self.num.append(node)

    def pop(self):
        self.num.pop()

    def top(self):
        length = len(self.num)
        return self.num[numlen-1]

    def min(self):
        return min(self.num)
