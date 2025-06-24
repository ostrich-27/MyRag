def sum(nums):
    if len(nums)==1:
        return nums[0]
    else:
        return nums[0]+sum(nums[1:])

def convert(n,base):
    str='0123456789ABCDEF'
    if n<base:
        return str[n]
    else:
        return convert(n//base,base)+str[n%base]
from DataStrcture.stack import Stack
def movedisk(tower1,tower2):
    print('from {} moving to {}'.format(tower1,tower2))
def movetower(height,from_tower,use_tower,to_tower):
    if height>=1:
        movetower(height-1,from_tower,to_tower,use_tower)
        movedisk(from_tower,to_tower)
        movetower(height-1,use_tower,from_tower,to_tower)

coinlist=[1,5,10,21,25]
table_coincount=[0]*64
table_coinused=[0]*64
def charge_1(amount):
    min_coin_num=amount
    if amount in coinlist:
        return 1
    else:
        for coin in [c for c in coinlist if c<amount]:
            coin_num=1+charge_1(amount-coin)
            if coin_num<min_coin_num:
                min_coin_num=coin_num
    return min_coin_num

def charge_2(amount):#增加了查询表
    min_coin_num=amount
    if amount in coinlist:
        table_coincount[amount]=1
        return 1
    elif table_coincount[amount]>0:
        return table_coincount[amount]
    else:
        for coin in [c for c in coinlist if c<=amount]:
            coin_num=1+charge_2(amount-coin)
            if coin_num<min_coin_num:
                min_coin_num=coin_num
                table_coincount[amount]=min_coin_num
    return min_coin_num


def charge_dp(amount):

    def coinprinter(coinused, amount):
        num=amount
        coin_list=[]
        while num>0:
            thiscoin=coinused[num]
            coin_list.append(thiscoin)
            num-=thiscoin
        return coin_list

    for every_amount in range(amount+1):
        min_coincounts=every_amount
        for coin in [c for c in coinlist if c<=every_amount]:
            if table_coincount[every_amount-coin]+1<min_coincounts:
                min_coincounts=table_coincount[every_amount-coin]+1
                table_coinused[every_amount]=coin
        table_coincount[every_amount]=min_coincounts

    print('Dynamic Programming table-->{}\ncoin used min-->{}\n'.format(table_coincount,table_coincount[amount],table_coinused))
    print('coin used -> {}'.format(coinprinter(table_coinused,amount)))