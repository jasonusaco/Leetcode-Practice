#链表的实现
class Node(object):

    def __init__(self,elem):
        self.elem = elem
        #初始设置下一个节点为空
        self.next = None

#实现单链表
class SingleLinkList(object):

    #使用一个默认参数，在传入头结点时则接收
    #在没有传入时，就默认头结点为空
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        #链表是否为空
        return self.__head == None

    def length(self):
        #链表长度

        #cur游标，用来移动遍历节点,从头结点开始
        #count记录数量
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        #遍历整个链表
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("\n")

    def add(self,item):
        #头部添加元素
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        #尾部添加元素
        node = Node(item)

        #如果链表为空的话就没有next了，所以要判断一下
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        #给指定位置添加元素

        #如果给的位置小于等于0的话直接当头结点插了
        if pos <= 0:
            self.add(item)
            
        #如果比链表还长，就插到尾结点
        elif pos > self.length() - 1:
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos -1:
                count += 1
                per = per.next

            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):
        #删除节点
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        #查看结点是否存在
        cur = self.__head
        while not cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
            
        
        
    
