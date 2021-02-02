N,*X = [int(x) for x in open(0).read().split()]
if N==2:
    print(X[1])
    print(X[0])
else:
    m=N//2
    sx=sorted(X)
    lx=set(sx[:m])
    lv=sx[m-1]
    rv=sx[m]
    for x in X:
        if x in lx:
            print(rv)
        else:
            print(lv)
