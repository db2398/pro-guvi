pc,vi=input().split()
AS=abs(len(pc)-len(vi))
for i in range(len(pc)):
  if len(vi)==1 and vi[i] in pc:
   break
  if pc[i]!=vi[i]:
   AS+=1
print(AS)
