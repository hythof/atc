H,W,*S = [x for x in open(0).read().split()]
H=int(H)
W=int(W)

ans=0
for h in range(1,H):
    for w in range(1,W):
        cnt=0
        for i in range(2):
            for j in range(2):
                if S[h-i][w-j]=="#":
                    cnt+=1
        if cnt%2==1:
            ans+=1

print(ans)
