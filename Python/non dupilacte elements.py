# l=[0,0,1,1,1,2,2,3,3,4]
# p=set(l)
# print(p)
# print(len(p))

# n=[1,2,1,3,2,4,5,4]
m=[]
n=list(map(int,input().split(" ")))
for i in n:
    if i not in m:
        m.append(i)
print(m)