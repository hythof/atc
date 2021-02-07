V,T,S,D = [int(x) for x in open(0).read().split()]
if T <= (D/V) <= S:
    print("No")
else:
    print("Yes")
