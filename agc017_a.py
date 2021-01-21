from collections import Counter

N,P,*A = [int(x) for x in open(0).read().split()]
c=Counter([a%2 for a in A])
if P==0:
    if c[1]==0:
        print(2**c[0])
    else:
        print(2**(N-1))
else:
    if c[1]==0:
        print(0)
    else:
        print(2**(N-1))
