S=input().strip()
T='keyence'
def check():
    i=0
    j=0
    while i<len(S) and j<len(T):
        if S[i] == T[j]:
            i+=1
            j+=1
        else:
            k=-(len(T)-j)
            return S[k:]==T[k:]
    return j==len(T)

if check():
    print('YES')
else:
    print('NO')
