A=25
B=25
C=10
if A is B:
    print("yes")
if A is not C:
    print("no")

n = int(input("enter the Number "))
l=[]
for i in range(0, n):
    x = int(input())
    l.append(x)
s=0
for i in range (0, n):
    s = s+l[i]
print(s);
print(l)
