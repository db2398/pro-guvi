#Triplet
s=int(input())
p=list(map(int,input().split()))
c=0
for i in range(0,s-2):
	for j in range(1,s-1):
		for k in range(2,s):
			if(p[i]<p[j] and p[j]<p[k]):
				c+=1
print(c)
