N,X,*XS = [int(x) for x in open(0).read().split()]

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

res=0
for x in XS:
    res=gcd(res, abs(x-X))
print(res)
