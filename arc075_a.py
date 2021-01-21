N,*S = [int(x) for x in open(0).read().split()]
S.sort()
ans=sum(S)
i=0
if ans%10==0:
    for s in S:
        if s%10!=0:
            print(ans-s)
            break
    else:
        print(0)
else:
    print(ans)
