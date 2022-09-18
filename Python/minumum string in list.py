l = ["flower","flow","fligt"]
# k=sorted(l)
# print(k)

minlen=len(l[0])
for i in range(len(l)):
    minlen=min(len(l[i]),minlen)
print(minlen)






