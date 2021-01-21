from collections import Counter
N,*AB = [int(x) for x in open(0).read().split()]
c=Counter(AB)
ab=sorted([(AB[i-1],AB[i]) if AB[i-1]<=AB[i] else (AB[i],AB[i-1]) for i in range(1, len(AB), 2)])
s=set([a for a,b in ab if a==b])
cc=Counter([a for a,b in ab])
for a,b in ab:
    if c[a]==1:
        s.add(a)
    elif c[b]==1:
        s.add(b)
    else:
        if a in s:
            s.add(b)
        elif b in s:
            s.add(a)
        else:
            s.add(a)
print(len(s))
