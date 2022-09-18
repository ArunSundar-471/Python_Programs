def calculate(m,n):
    s=0
    for i in range(m,n):
        if(i % 3==0)and (i%5==0):
            s=s+i
    return s


m=int(input())
n=int(input())
print(calculate(m,n))