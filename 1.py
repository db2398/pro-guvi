santhosh = int(input())
d=[]
for i in range(0,santhosh):
 lan=input()
 d.append(lan)
thissss=[]
for i in zip(*d):
 if(i.count(i[0])==len(i)):
  thissss.append(i[0])
 
 else:
  break
print(''.join(thissss))
