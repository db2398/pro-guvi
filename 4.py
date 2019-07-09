days,gone=map(str,input().split())
wave=0
if len(days)>len(gone):
  days,gone=gone,mah
i=0
while i<len(days):
  silent+=(ord(gone[i])-ord(days[i]))
  i+=1
for i in range(i,len(gone)):
  silent+=ord(gone[i])-ord('a')+1
print(silent)
