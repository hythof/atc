N=int(input())
nums=[]
for i in range(1,int((2*N)**0.5)+1):
    if (2*N)%i==0:
        nums.append(i)
ans=0
for n in nums:
    if (2*N//n)&1 != n&1:
        ans+=1
print(ans*2)
