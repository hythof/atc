N,M,*X = [int(x) for x in open(0).read().split()]
if N>=M:
    print(0)
else:
    X.sort()
    gaps = [abs(a-b) for a,b in zip(X, X[1:])]
    gaps.sort()
    mn=M-N
    print(sum(gaps[:mn]))
