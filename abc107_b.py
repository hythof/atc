H,W,*A = [x for x in open(0).read().split()]
H=int(H)
W=int(W)
whites=[0]*W
for a in A:
    for i,c in enumerate(a):
        if c=='.':
            whites[i]+=1
checks=[white != H for white in whites]
wline='.'*W
for a in A:
    if a == wline:
        continue
    print(''.join([c for i,c in enumerate(a) if checks[i]]))
