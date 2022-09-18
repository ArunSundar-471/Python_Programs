def myfunc1(n):
  return lambda a : a * n

mydoubler = myfunc1(2)

print(mydoubler(11))



def myfunc2(n):
  return lambda a : a * n

x = myfunc2(1)
y = myfunc2(3)

print(x(11))
print(y(11))
