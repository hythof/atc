N,M = [int(x) for x in open(0).read().split()]
if M<=N*2:
    print(M//2)
else:
    c=M-N*2
    ans=N+c//4
    print(ans)
