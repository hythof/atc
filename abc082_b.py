s,t = [x for x in open(0).read().split()]
s=''.join(sorted(list(s)))
t=''.join(sorted(list(t), reverse=True))
if s<t:
    print('Yes')
else:
    print('No')
