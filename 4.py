vs,vit1=map(str,input().split())
was=0
if len(vs)>len(vit1):
  vs,vit1=vit1,dbj
i=0
while i<len(vs):
  was+=(ord(vit1[i])-ord(vs[i]))
  i+=1
for i in range(i,len(vit1)):
  was+=ord(vit1[i])-ord('a')+1
print(was)
