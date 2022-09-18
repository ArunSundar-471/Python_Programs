size=int(input())
e=[]
o=[]
for i in range(size):
    print("element at",i,"index ",end='')
    k=int(input())
    if i %2==0:
        e.append(k)
    else:
        o.append(k)
e.sort()
o.sort()
print("even array:",*e)
print("odd array:",*o)

