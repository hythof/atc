C=[list(map(int,input().split())) for _ in range(3)]
def check():
    for a0 in range(101):
        for a1 in range(101):
            for a2 in range(101):
                b0 = C[0][0]-a0
                b1 = C[0][1]-a0
                b2 = C[0][2]-a0
                if C[1][0]-a1 == b0 and \
                   C[1][1]-a1 == b1 and \
                   C[1][2]-a1 == b2 and \
                   C[2][0]-a2 == b0 and \
                   C[2][1]-a2 == b1 and \
                   C[2][2]-a2 == b2:
                       return True

if check():
    print('Yes')
else:
    print('No')
