#Triplet
u=int(input())
o=list(map(int,input().split()))
c=0
for i in range(0,u-2):
	for j in range(1,u-1):
		for k in range(2,u):
			if(o[i]<o[j] and o[j]<o[k]):
				c+=1
print(c)
