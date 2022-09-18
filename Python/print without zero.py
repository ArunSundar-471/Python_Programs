# 1210
# 121


def FindAutoCount(n,s):
  for i in s:
    if i=='0':
      n=n-1
  print(n)


s=input()
n=len(s)
FindAutoCount(n,s)