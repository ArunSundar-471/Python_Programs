l = ["flower","flow","fligt"]
maxx=0
for j in l:
    if len(j)>maxx:
        maxx=len(j)
        word=j
print("max word:",word)

minn=len(l[0])
for i in l:
    if len(i)<minn:
        minn=len(i)
        word=i
print("min word:",word)


