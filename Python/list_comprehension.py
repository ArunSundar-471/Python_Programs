fruits=["fruit","apple","cherry","mango"]
l=[]
for i in fruits:
    if 'a' in i:
        l.append(i)
print(l)

l=[i for i in  fruits if 'e' in i]
print(l)