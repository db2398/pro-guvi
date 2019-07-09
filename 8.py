import math
n11,m11=map(int,input().split())
sp=[]
aa=list(map(int,input().split()))
for i in range(0,m11):
    l,h=map(int,input().split())
    sp.append([l,h])
for i in sp:
    ss=i[0]-1
    oo=i[1]-1
    print(math.gcd(aa[ss],aa[oo]))
