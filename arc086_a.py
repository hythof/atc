from collections import Counter
N,K,*A = [int(x) for x in open(0).read().split()]
c=Counter(A)
s=c.most_common()[K:]
ans=sum([n for _,n in s])
print(ans)
