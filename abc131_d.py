N,*AB = [int(x) for x in open(0).read().split()]
BA=sorted([(AB[i+1],AB[i]) for i in range(0,len(AB),2)])
def check():
    t=0
    for b, a in BA:
        t+=a
        if t>b:
            return False
    return True
if check():
    print('Yes')
else:
    print('No')
