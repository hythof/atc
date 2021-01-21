N,T,*A = [int(x) for x in open(0).read().split()]
ans=0
for t1,t2 in zip(A,A[1:]):
    ans+=min(T, t2-t1)
ans+=T
print(ans)
