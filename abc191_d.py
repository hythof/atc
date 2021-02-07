from decimal import Decimal
import math
ans=0
for y in range(math.ceil(Y-R),math.floor(Y+R)+1):
    d=(R**2-(Y-y)**2).sqrt()
    x1=math.ceil(X-d)
    x2=math.floor(X+d)
    if x1<=x2:
        ans+=x2-x1+1
print(ans)
