H,W,*S = [x for x in open(0).read().split()]
H=int(H)
W=int(W)
dp=[[100*100]*W for _ in range(H)]
dp[0][0] = 0 if S[0][0]=='.' else 1
for i in range(1,H):
    dp[i][0] = dp[i-1][0] + (S[i][0] == '#' and S[i-1][0] == '.')
for i in range(1,W):
    dp[0][i] = dp[0][i-1] + (S[0][i] == '#' and S[0][i-1] == '.')
for h in range(1,H):
    for w in range(1,W):
        dp[h][w] = min(
            dp[h][w-1] + (S[h][w] == '#' and S[h][w-1] == '.'),
            dp[h-1][w] + (S[h][w] == '#' and S[h-1][w] == '.'))
print(dp[H-1][W-1])
