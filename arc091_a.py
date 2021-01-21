N,M = [int(x) for x in open(0).read().split()]
if N==1 and M==1:
    print(1)
elif min(N,M)==1:
    print(max(N,M)-2)
elif min(N,M)==2:
    print(0)
else:
    ans=N*M-(2*N+2*M-4)
    print(ans)
