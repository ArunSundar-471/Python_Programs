from itertools import combinations
from itertools import permutations

l=list(map(int,input().split()))

p=[]
perm=permutations(l,2)

for i in perm:
    p.append(i)
print(p)
s=[]
com=combinations(l,2)
for i in com:
    s.append(i)
print(s)