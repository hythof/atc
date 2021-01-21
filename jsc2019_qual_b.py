from collections import Counter
N,K,*A = [int(x) for x in open(0).read().split()]

ans=0
mod=10**9+7
for i in range(N-1,-1,-1):
    t1=0
    for j in range(i-1,-1,-1):
        if A[i] < A[j]:
            t1+=1
    t2=0
    for j in range(N):
        if A[i] < A[j]:
            t2+=1
    ans+=t1*K + t2*((K*(K-1))//2)

print(ans%mod)
