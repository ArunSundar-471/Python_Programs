# 111,121   not uniqu
# 105 unique

# print(set([1,2,3,2,1]))   #unique numbers
first=int(input())
last=int(input())
p=0
for i in range(first,last):
    s=set(list(str(i)))
    print(s)
    if len(s)==len(list(str(i))):
        p=p+1
print(p)


