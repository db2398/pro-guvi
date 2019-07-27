put=int(input())
laas=input().split()
sas=[]
for i in range(nati):
    suri=laas[i]
    for j in range(i+1,nati):
        if(int(laas[i])<int(laas[j]))and (int(laas[j-1])<int(laas[j])):
            suri+=laas[j]
        else:
            break
    sas.append(len(suri))
print(max(sas))
