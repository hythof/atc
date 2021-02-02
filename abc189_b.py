N,X,*VP = [int(x) for x in open(0).read().split()]
a=0
hit=-1
x=X*100
for i in range(0, len(VP), 2):
    v=VP[i]
    p=VP[i+1]
    a+=v*p
    if a>x:
        hit=1+i//2
        break
print(hit)
