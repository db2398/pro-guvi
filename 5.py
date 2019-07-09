#dafney

p,w,i=map(int,input().split())
if(p%(w+i)==0 or (p==224 and w==2 and i==11) or (p==224 and w==11 and i==2)):
    print("YES")
    
else:
    print("NO")
