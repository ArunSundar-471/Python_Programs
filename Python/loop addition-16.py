n=int(input())
s=0
p=11
k=0
for i in range(1,p):
    s=n+s
    k=s+k
    if(i==p-1):
        print(n*10)
    else:
     print(s,end=',')

print(k)