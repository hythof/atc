S=input()
l=len(S)
i=0
ans=[0]*l
while i<l:
    j=i
    while j<l and S[j]=='R': j+=1
    k=j
    while k<l and S[k]=='L': k+=1
    lr = list(range(i,k+1 if k==l-1 else k))
    even=len([n for n in lr if n%2==0])
    odd=len(lr)-even
    ans[j-1] = even if (j-1)%2==0 else odd
    ans[j] = even if j%2==0 else odd
    i=k
print(" ".join(map(str, ans)))
