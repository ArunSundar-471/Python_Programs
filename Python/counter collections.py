from collections import Counter,defaultdict
p="missippi"
s=Counter(p)
#print based on the highest values
print(s)

word="mississsippi"
counter=defaultdict(int)
for i in word:
  counter[i]=counter[i]+1
print(counter)