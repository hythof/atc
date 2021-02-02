N,S,D,*XY = [int(x) for x in open(0).read().split()]
xy=[(XY[i],XY[i+1]) for i in range(0, len(XY), 2)]
ans=[(x,y) for x,y in xy if y>D and x<S]
if ans:
    print('Yes')
else:
    print('No')
