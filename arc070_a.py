X=int(input())
x=0
for i in range(1,10**9+1):
    x+=i
    if x>=X:
        break
print(i)
