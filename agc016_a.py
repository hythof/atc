from collections import defaultdict
S=input()

ans=1000
for i in range(26):
    c=chr(i+97)
    if c not in S:
        continue
    *heads,tail = map(len, S.split(c))
    ans=min(ans, max(max(heads), tail))

print(ans)
