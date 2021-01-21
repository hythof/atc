N,M,*SC = [int(x) for x in open(0).read().split()]
ary=[None]*N
for i in range(0,len(SC),2):
    s=SC[i]
    c=SC[i+1]
    index=s-1
    sv = ary[index]
    if s>N:
        print(-1)
        break
    if sv is None:
        ary[index] = c
        continue
    if sv != c:
        print(-1)
        break
else:
    if N==1:
        if ary[0] is None:
            print(0)
        else:
            print(ary[0])
    else:
        if ary[0]==0:
            print(-1)
        else:
            if ary[0] is None:
                ary[0]=1
            print(''.join(['0' if a is None else str(a) for a in ary]))
