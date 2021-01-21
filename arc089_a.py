N,*A = [int(x) for x in open(0).read().split()]
def check():
    bx=0
    by=0
    bt=0
    for i in range(0, len(A), 3):
        t=A[i]
        x=A[i+1]
        y=A[i+2]
        d=abs(bx-x)+abs(by-y)
        if (t-bt) < d:
            return False
        if (t-bt-d)%2==1:
            return False
        bx=x
        by=y
        bt=t
    return True

if check():
    print('Yes')
else:
    print('No')
