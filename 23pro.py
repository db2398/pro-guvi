db=int(input())
mah=2**db
p=[]
for i in range(0,mah):
    l=bin(i)[2:].pfill(db)
    if(len(l)<len(bin(2**db-1)[2:])):
        p.append([l.count("1"),l])
    else:
        p.append([l.count("1"),l])
p.sort()
for i in range(len(p)):
    print(p[i][1])
