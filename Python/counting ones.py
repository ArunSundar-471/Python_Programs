str=input()
s=0
m=0
for i in range(len(str)):
    if (str[i]=='1'):
        s=s+1
    else:
        if m< s:
            m=s
            s=0
print(m)