from collections import Counter
S=input()
c=Counter(S)
_,n=c.most_common()[0]
l=len(S)
if l>=n*3-2:
    print('YES')
else:
    print('NO')
