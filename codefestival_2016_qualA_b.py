N,*A = [int(x) for x in open(0).read().split()]
A=[a-1 for a in A]
d={}
for i,a in enumerate(A):
    d[i]=a
ans=0
for i in range(N):
    a=d[i]
    if a in d and d[a]==i:
        ans+=1
print(ans//2)
