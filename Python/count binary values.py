# 3
# 101
# 011
# yes
n=int(input())
a=input()
b=input()
c=0
d=0
e=0
f=0
for i in a :
    if i=='0':
        c=c+1
    else:
        d=d+1

for j in b:
    if j=='0':
        e=e+1
    else:
        f=f+1

if(c==e and d==f):
    print("yes")
else:
    print("no")