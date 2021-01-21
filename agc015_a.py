N,A,B = [int(x) for x in open(0).read().split()]
if A>B:
    print(0)
elif N==1:
    if A==B:
        print(1)
    else:
        print(0)
else:
    min_=(N-1) * A + B
    max_=A + (N-1) * B
    print(max_-min_+1)
