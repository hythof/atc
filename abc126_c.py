N,K = [int(x) for x in open(0).read().split()]
ans=0
for i in range(1,N+1):
    p=i
    odds=1.0/N
    while p<K:
        p*=2
        odds/=2
    ans+=odds
print(ans)
