def double(x):
    return x**2
y=[double(x) for x in range(10)]
print(y)

p=[i for i in 'humans']
print(p)
l=[j for j in range(20) if j%2==0]
print(l)
p=["even" if i%2==0 else "odd" for i in range(10) ]
print(p)
