path=int(input())
bin=[int(i) for i in input().split()]
pest=0
for k in range(path):
   for j in range(k):
      if bin[j]<bin[k]:
         pest+=bin[j]
print(pest) 
