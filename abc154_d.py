N,K,*A = [int(x) for x in open(0).read().split()]
A=[(a+1)/2 for a in A]
dp=[A[0]]+[0]*(N+K)
for i in range(1,N):
    dp[i]=A[i]+dp[i-1]
index=0
up=sum(A[:K])
for i in range(N):
    up=max(up,dp[i+K]-dp[i])
print(up)
