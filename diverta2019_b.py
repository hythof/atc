R,G,B,N = [int(x) for x in open(0).read().split()]
ans=0
for r in range(N+1):
    for g in range(N+1):
        nrg=N-r*R-g*G
        if nrg<0:
            continue
        if nrg % B == 0:
            ans+=1
print(ans)
