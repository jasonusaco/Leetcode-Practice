class Queue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    #入队
    def enqueue(self.x):
        self.queue.append(x)

    #出列,删除表开头的元素，因为是先进先出
    def dequeue(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError, 'queue is empty'

    def size(self):
        return len(self.queue)
