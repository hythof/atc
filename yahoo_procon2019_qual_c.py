K,A,B = [int(x) for x in open(0).read().split()]
if B-A<2:
    print(K+1)
else:
    b=1
    i=0
    while i<K:
        if K-i>=2 and b>=A:
            i+=2
            b-=A
            b+=B
        else:
            i+=1
            b+=1
    print(b)
