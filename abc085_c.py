N,Y = [int(x) for x in open(0).read().split()]
def check():
    for i in range(N+1):
        for j in range(N-i+1):
            k=N-i-j
            if 10000*i+5000*j+k*1000==Y:
                print(i,j,k)
                return
    print(-1,-1,-1)
check()
