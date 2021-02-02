A,B,C = [int(x) for x in open(0).read().split()]
if C==0:
    if A<=B:
        print('Aoki')
    else:
        print('Takahashi')
else:
    if B<=A:
        print('Takahashi')
    else:
        print('Aoki')
