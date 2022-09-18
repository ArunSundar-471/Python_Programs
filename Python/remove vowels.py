a=input()
s=""
p=""
c=0
vowels=['a','e','i','o','u']

for i in a:
    if i in vowels:
        c=c+1
if c==1:
    for i in a:
        if i not in vowels:
            s=s+i
    print(s)
else:
    for i in a:
        s=s+i
    print(s)





# for i in range(len(a)):
#     if a[i] not in vowels:
#         s=s+a[i]
# print(s)
