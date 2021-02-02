L,R = [int(x) for x in open(0).read().split()]
s=set()
for x in range(L,R+1):
    m=x%2019
    if m in s:
        break
    s.add(m)
l=list(s)
n=2019
for i in range(len(l)):
    for j in range(i+1, len(l)):
        n=min(n, (l[i]*l[j])%2019)
print(n)
