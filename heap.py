class BinaryHeap_Min:
    '''
    二叉堆--最小堆
    '''
    def __init__(self):
        self.items=[0]
        self.currentsize=0

    def minchild(self,i):
        '''
        接收父节点 返回最小的子节点
        :param i:
        :return:
        '''
        if i*2+1>self.currentsize:
            return i*2
        else:
            if self.items[i*2]<=self.items[i*2+1]:
                return i*2
            else:
                return i*2+1

    def percUP(self,i):
        '''
        为下层节点找到合适位置-->自下而上 上调子节点
        :param i:接收子节点
        :return:
        '''
        while i//2>0:
            if self.items[i]<self.items[i//2]:
                self.items[i],self.items[i//2]=self.items[i//2],self.items[i]
            i=i//2

    def percDown(self,i):
        '''
        为上层节点找到合适的位置 -->自上而下 下降父节点
        :param i:接收父节点
        :return:
        '''
        while i*2<=self.currentsize:
            mc=self.minchild(i)
            if self.items[i]>self.items[mc]:
                self.items[i],self.items[mc]=self.items[mc],self.items[i]
            i=mc

    def insert(self,k):
        self.items.append(k)
        self.currentsize+=1
        self.percUP(self.currentsize)

    def findMin(self):
        return self.items[1]

    def delMin(self):
        '''
        取出最小值
        :return:
        '''
        value=self.items[1]
        self.items[1]=self.items[self.currentsize]
        self.currentsize=self.currentsize-1
        self.items.pop()
        self.percDown(1)
        return value

    def isEmpty(self):
        if self.currentsize==0:
            return True
        else:
            return False

    def size(self):
        return self.currentsize

    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentsize=len(alist)
        self.items=[0]+alist[:]
        while i >0:
            self.percDown(i)
            i=i-1