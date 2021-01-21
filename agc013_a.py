N,*A = [int(x) for x in open(0).read().split()]
ans=0
i=j=0
A+=[0,1]
while i<N:
    while i<N and A[i]<=A[i+1]: i+=1
    while j<N and A[j]>=A[j+1]: j+=1
    i=j=max(i,j)+1
    ans+=1
print(ans)
