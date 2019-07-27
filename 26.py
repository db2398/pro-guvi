pot = int(input())
lays = list(map(int, input().split()))
maximum = 0
ccss = 0
any = lays[0]
for i in range(0,pot-1):
    if any < lays[i+1]:
        ccss +=1
        any = lays[i+1]
    else:
        if max(lays[i+1:]) < any:
            any = lays[i+1]
print(ccss+1)
