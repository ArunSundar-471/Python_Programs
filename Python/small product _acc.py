def productsmall(n,arr):
    arr.sort()
    p=arr[0]+arr[1]
    if(p<n):
        return arr[0]*arr[1]
    else:
        return -1




n=int(input())
arr=list(map(int,input().split()))
print(productsmall(n,arr))
