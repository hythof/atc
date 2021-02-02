from collections import Counter
N,*A = [int(x) for x in open(0).read().split()]
c=Counter(A)
bars = [k for k in sorted(c.keys(),reverse=True) if c[k]>=2][:2]
if len(bars)>=1 and c[bars[0]]>=4:
    print(bars[0]**2)
elif len(bars)==2:
    print(bars[0]*bars[1])
else:
    print(0)
