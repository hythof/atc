N,S,T = [x for x in open(0).read().split()]
N=int(N)
def find():
    for i in range(N):
        if T.startswith(S[i:]):
            return N-i
    return 0
print(N*2-find())
