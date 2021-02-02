from collections import defaultdict

N,M,*ABKC=[int(x) for x in open(0).read().split()]
AB=[(ABKC[i], ABKC[i+1]) for i in range(0, M*2, 2)]
K=ABKC[M*2]
C=ABKC[M*2+1:]

class UF:
    def __init__(self, n):
        self.n=n
        self.parents=[-1]*n
    def find(self, x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.parents[x]>self.parents[y]:
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    def size(self,x):
        return -self.parents[self.find(x)]
    def members(self,x):
        root=self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

uf=UF(N+1)
for a,b in AB:
    uf.union(a,b)

if N==uf.size(1):
    c=set(C)
    ans=K
    for i in range(1,K+1):
        g = uf.members(i)
        if i in g:
            continue
        ans+=1
    print(ans)
else:
    print(-1)

print(AB,K,C)
