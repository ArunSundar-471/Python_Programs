a = 0
b = 1
c = 0,

n = int(input())
print(a)
print(b)
c = a + b

while c <= n - 1:
  print (c)
  a = b
  b = c
  c = a + b


