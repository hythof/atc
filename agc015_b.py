S=input()
l=len(S)
ans=0
for i in range(l):
    if S[i]=='D':
        ans+=l-i-1
    else:
        ans+=i
    ans+=l-1
print(ans)
