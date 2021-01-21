N,*H = [int(x) for x in open(0).read().split()]
def solve(l, r):
    if l>r:
        return 0
    min_=min(H[l:r+1])
    for i in range(l,r+1):
        H[i]-=min_
    count=min_
    i=l
    while i<r:
        while i<=r and H[i]==0: i+=1
        s=i
        while i<=r and H[i]>0: i+=1
        count+=solve(s,i-1)
    return count

print(solve(0, len(H)-1))
