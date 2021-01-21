from collections import Counter
N,*A = [int(x) for x in open(0).read().split()]
print(len([x for x in Counter(A).values() if x%2==1]))
