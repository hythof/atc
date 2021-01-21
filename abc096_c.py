H,W,*SHW = [x for x in open(0).read().split()]
H=int(H)
W=int(W)

def isBlack(x,y):
    if x < 0 or y < 0 or x >= W or y >= H:
        return False
    return SHW[y][x]=='#'

def isIndipendent(x,y):
    if not isBlack(x,y):
        return False
    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        if isBlack(x+i,y+j):
            return False
    return True

def check():
    for h in range(H):
        for w in range(W):
            if isIndipendent(w,h):
                return False
    return True

if check():
    print('Yes')
else:
    print('No')
