from collections import Counter
N,*DMT=[int(x) for x in open(0).read().split()]
M=DMT[N]
D=DMT[:N]
T=DMT[N+1:]
t=Counter(T)
d=Counter(D)
if not t-d:
    print('YES')
else:
    print('NO')
