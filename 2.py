#mano
from itertools import combinations
s,t=input().split()
t=int(t)
top=[]
van=len(s)-t
fake=combinations(s,van)
for i in list(fake):
  top.append("".join(i))
print(min(top))
