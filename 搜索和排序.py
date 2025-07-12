from DataStrcture.hashtable import Hashtable

import random

foo1=[]

for _ in range(1,201):
    foo1.append(random.randint(1,1001))

print(foo1)



def bubblesort(lis):
    '''
    descending/ascending
    :param lis:
    :return:
    '''
    for i in range(len(lis)):
        for k in range(len(lis)):
            if lis[i]>lis[k]:
                lis[i],lis[k]=lis[k],lis[i]
            else:
                continue

def shortbubblesort(lis):
    '''
    descending
    :param lis:
    :return:
    '''
    exchange=True
    begin=0
    while exchange:
        for i in range(begin,len(lis)):
            exchange=False
            for k in range(begin,len(lis)):
                if lis[i]<lis[k]:
                    exchange=True
                    lis[i],lis[k]=lis[k],lis[i]
            begin+=1

def selectionsort(lis):
    '''
    descending
    :param lis:
    :return:
    '''
    begin=0
    for fileslot in range(begin,len(lis)):
        maxpositon=begin
        for index in range(fileslot+1,len(lis)):
            if lis[index]>lis[maxpositon]:
                maxpositon=index
        lis[fileslot],lis[maxpositon]=lis[maxpositon],lis[fileslot]
        begin+=1

def insertsort(lis):



bubblesort(foo1)

print('-'*100)
print('after bubblesort -->{}'.format(foo1))


