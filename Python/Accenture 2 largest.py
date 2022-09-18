a=list(map(int,input().split()))
E=[]
O=[]
for i in range(len(a)):
    if i%2==0:
        E.append(a[i])
    else:
        O.append(a[i])
E.sort()
O.sort()
k=E[-2]
l=O[-2]
print(k+l)
# print(E)
# print(O)