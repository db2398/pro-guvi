daf,sun=input().split()
uff=abs(len(daf)-len(sun))
for i in range(len(bhav)):
  if len(sun)==1 and sun[i] in daf:
   break
  if daf[i]!=sun[i]:
   uff+=1
print(uff)
