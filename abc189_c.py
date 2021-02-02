N,*A = [int(x) for x in open(0).read().split()]
ans=max(A)
for i in range(N):
    a=A[i]
    n=1
    for j in range(i+1,N):
        a=min(a,A[j])
        n+=1
        ans=max(ans,a*n)
print(ans)
