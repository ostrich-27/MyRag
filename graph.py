class Vertex:
    def __init__(self,key):
        self.id=key
        self.to={}
    def addneighbor(self,nbr,weight=0):
        self.to[nbr]=weight
    def __str__(self):
        return str(self.id)+'To:'+str([x.id for x in self.to])
    def getto(self):
        return self.to.keys()
    def getid(self):
        return self.id
    def getweight(self,nbr):
        return self.to[nbr]

class Graph():#邻接表
    def __init__(self):
        self.vertlist={}
        self.numvertices=0
    def addvert(self,key):
        self.numvertices+=1
        v=Vertex(key)
        self.vertlist[key]=v
        return v
    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self, item):
        return item in self.vertlist
    def addegde(self,f,t,cost=0):
        if f not in self.vertlist:
            nv=self.addvert(f)
        if t not in self.vertlist:
            nv=self.addvert(t)
        self.vertlist[f].addneighbour(self.vertlist[t],cost)
    def getVertices(self):
        return self.vertlist.keys()
    def __iter__(self):
        return iter(self.vertlist.values())