lis= [2,5,-1,7,8,-2]
#using three for loops
com = list(range(1,len(lis)+1))
for i in lis:
    for j in com:
        if i == j :
            com.remove(j)
print(com[0])

#using 2 for loops
lis= [2,5,-1,7,8,-2]

comp = list(range(1,len(lis)+1))
for i in range(len(lis)):
    if(lis[i]<=len(lis)) & (lis[i]>0):
        comp.remove(lis[i])
print(comp)
#efficient method
comp1 = list(range(1,len(lis)+1))
for i in range(len(lis)):
    if(lis[i]<=len(lis)) & (lis[i]>0):
     comp1[lis[i]-1]=0
print(comp1)
for k in comp1:
    if k !=0:
     print(k)
     break;
