def nearestnumb(num,n):
    a=num//n
    c=a*n
    d=(a+1)*n
    # print(c,d)
    p=num-c
    k=d-num
    # print(p,k)
    if(p<k):
        return c
    else:
        return d







num=int(input())
n=int(input())
print(nearestnumb(num,n))