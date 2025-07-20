class Queue:
    '''
    队列--以list的头部为底 以list的尾部的为顶
    '''
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        '''
        取走队列开头的元素
        :return:
        '''
        return self.items.pop()

    def peek(self):
        '''
        检查队列头的元素
        :return:
        '''
        return self.items[(len(self.items)-1)]

class Deque:
    '''
    双端队列
    '''
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def addFront(self,item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)