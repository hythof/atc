S=input()
ans=[]
for s in S:
    if s=='B':
        if ans:
            ans.pop()
    else:
        ans.append(s)
print(''.join(ans))
