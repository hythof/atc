N,X,*A = [int(x) for x in open(0).read().split()]
print(" ".join([str(a) for a in A if a != X]))
