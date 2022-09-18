def password(s,n,c):
    if len<=8:
        return 0
    if c.isdigit():
        return 0
    c=0
    num=0
    for i in range(len):
        if (s[i] == ' ' or s[i] == '+'):
            return 0
        if(s[i]>='A' and s[i]<='Z'):
            c=c+1
        if s[i].isdigit():
            num=num+1
    if c>0 and num>0:
        return 1
    else:
        return 0

s=input()
len=len(s)
c=s[0]
if(password(s,len,c)):
    print("valid")
else:
    print("invalid")