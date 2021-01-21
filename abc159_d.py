from collections import Counter

def count(n):
    return n*(n-1)//2

N,*A = [int(x) for x in open(0).read().split()]
c=Counter(A)
s=sum([count(v) for v in c.values()])
for a in A:
    print(s-count(c[a])+count(c[a]-1))
