res=input()
n=len(s)
k=int(input())
p=""
for i in range(n):
    if k<n:
        p=p+s[k-1]
        break
    else:
        print("-1")
        break
print(p)
 # a 2 b 2 c 2 d 1
 # 0 1 2 3 4 5 6 7
 # 5
