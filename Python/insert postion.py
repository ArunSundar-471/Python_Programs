def insert(l):
    l.append(target)
    k = l.sort()
    print(k.index(target))


l=[1,3,5,6]
target = input()
n=len(l)
if target in  l:
    print(l.index(target))
else:
    insert(l)
