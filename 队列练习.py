from DataStrcture.queue import Queue,Deque
import random
import time
def hotpotato(names,num,pattren=None):
    '''
    传土豆 关键是构成一个环
    :param namelist:
    :param num:
    :return:
    '''
    q = Queue()
    for name in names:
        q.enqueue(name)
    if pattren==1:#击鼓传花
        index=0
        while index<num:
            q.enqueue(q.dequeue())
            index+=1
        return q.peek()
    else:#热土豆
        while q.size()>1:
            for i in range(num):
                q.enqueue(q.dequeue())
            q.dequeue()
            print(q.items)
        return q.peek()

class Printer:
    def __init__(self,ppm):
        self.currenttask=None
        self.PagesPerMinutes=ppm
        self.timesremaining=0

    def isBuzy(self):
        if self.currenttask!=None:
            return True
        else:
            return False

    def tick(self):
        if self.currenttask!=None:
            self.timesremaining-=1
            if self.timesremaining<0:
                self.currenttask=None

    def startnewtask(self,newtask):
        self.currenttask=newtask
        self.timesremaining=newtask.pages*60/self.PagesPerMinutes

class Task:
    def __init__(self,timestamp):
        self.pages=random.randrange(1,21)
        self.create_time=timestamp

    def waittime(self,timestamp):
        return timestamp-self.create_time

def simulation(simulation_times,printer_speed):
    PrintQueue=Queue()
    waittime=[]
    myprinter=Printer(printer_speed)
    for currenttime in range(simulation_times):
        task_possible=random.randrange(1,181)
        if task_possible==180:
            task=Task(currenttime)
            PrintQueue.enqueue(task)
        if not myprinter.isBuzy() and not PrintQueue.isEmpty():
            newtask=PrintQueue.dequeue()
            myprinter.startnewtask(newtask)
            waittime.append(newtask.waittime(currenttime))
        myprinter.tick()
    try:
        averagewaittime=sum(waittime)/len(waittime)
    except:
        return print('None')
    print('Average wait {} seconds \t {} tasks remaining'.format(averagewaittime,PrintQueue.size()))


def palchecker(str):
    dq=Deque()
    for i in str:
        dq.addRear(i)
    equal=True
    while equal and dq.size()>1:
        if dq.removeFront()==dq.removeRear():
            equal=True
        else:
            return False
    return True
