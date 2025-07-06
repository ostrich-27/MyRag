import string
import operator
from DataStrcture.trees import BinaryTrees
from DataStrcture.stack import Stack
from DataStrcture.heap import BinaryHeap

def parsetree(str):
    '''
    解析树
    :param str:
    :return:
    '''
    s=Stack()
    t0=BinaryTrees(None)
    s.push(t0)
    currenttree=t0
    for i in str:
        if i =="(":
            currenttree.insertleftchild(None)
            s.push(currenttree)
            currenttree=currenttree.getleftchild()
        elif i in string.digits:
            currenttree.setroot(int(i))
            currenttree=s.pop()
        elif i in '/*-+':
            currenttree.setroot(i)
            currenttree.insetrightchild(None)
            s.push(currenttree)
            currenttree=currenttree.getrightchild()
        elif i == ')':
            currenttree=s.pop()
        else:
            pass
    return t0

def parsetree_evaluate(parsetree):
    opers={'/':operator.truediv,'*':operator.mul,'-':operator.sub,'+':operator.add}
    left=parsetree.getleftchild()
    right=parsetree.getrightchild()
    if left and right:
        fn=opers[parsetree.getroot()]
        return fn(parsetree_evaluate(left),parsetree_evaluate(right))
    else:
        return parsetree.getroot()

def proorder(tree):#前序遍历 访问根节点 递归访问左子树 递归访问右子树
    if tree:
        print(tree.getroot(),end='')
        proorder(tree.getleftchild())
        proorder(tree.getrightchild())

def inorder(tree):#中序遍历 递归遍历左子树 访问根节点 递归访问右子树
    if tree:
        inorder(tree.getleftchild())
        print(tree.getroot(),end='')
        inorder(tree.getrightchild())

def postorder(tree):#后序遍历 递归访问右子树 递归访问左子树 访问根节点
    if tree:
        postorder(tree.getleftchild())
        postorder(tree.getrightchild())
        print(tree.getroot(),end='')

def evalpostorder(tree):
    opers = {'/': operator.truediv, '*': operator.mul, '-': operator.sub, '+': operator.add}
    left=None
    right=None
    if tree:
        left=evalpostorder(tree.getleftchild())
        right=evalpostorder(tree.getrightchild())
        if left and right:
            return opers[tree.getroot()](left,right)
        else:
            return tree.getroot()

def evalinorder(tree):
    val=''
    if tree:
        if tree.getrightchild():
            val='('+evalinorder(tree.getleftchild())
        else:
            val=''+evalinorder(tree.getleftchild())
        val+=str(tree.getroot())
        if tree.getrightchild():
            val=val+evalinorder(tree.getrightchild())+')'
        else:
            val=val+evalinorder(tree.getrightchild())
    return val
