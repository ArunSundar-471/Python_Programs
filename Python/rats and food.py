def func(arr,rats,food,n):
    if n==0:
        return -1
    total=rats*food
    s=0
    i=0
    for i in range(n):
        s=s+arr[i]
        if(s>=total):
            break
    if(total>s):
            return 0
    return i+1




rats=int(input())
food=int(input())
n=int(input())
arr=list(map(int,input().split()))
print(func(arr,rats,food,n))