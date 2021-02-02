N,*S = [x for x in open(0).read().split()]
N=int(N)
if all([s=='AND' for s in S]):
    print(1)
elif all([s=='OR' for s in S]):
    print(2**(N+1)-1)
else:
    ans=2**(N+1)
    for i in range(N):
        s=S[i]
        if s=='AND':
            ans-=(2**(i+1))
    print(ans-1)
