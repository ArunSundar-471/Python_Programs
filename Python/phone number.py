n=int(input())
for i in range(n):
  k=input()
  l=""
  for i in k:
    s=int(i)
    if s%2!=0:
        l=l+i
  for i in k[::-1]:
    s=int(i)
    if s%2==0:
        l=l+i
  print(l)
