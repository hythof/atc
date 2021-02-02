N,M,*ABKCD = [int(x) for x in open(0).read().split()]
AB=[(ABKCD[i], ABKCD[i+1]) for i in range(0, M*2, 2)]
K=ABKCD[M*2]
CD=[(ABKCD[i], ABKCD[i+1]) for i in range(M*2+1, len(ABKCD), 2)]

ans=0
for i in range(2**K):
    s=set([CD[j][int(bool(i&(1<<j)))] for j in range(K)])
    ans=max(ans, sum([a in s and b in s for a,b in AB]))

print(ans)
