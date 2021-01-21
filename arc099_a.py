from math import ceil
N,K,*A = [int(x) for x in open(0).read().split()]
if K>=N:
    print(1)
else:
    ans=ceil((N-K)/(K-1)) + 1
    print(ans)
