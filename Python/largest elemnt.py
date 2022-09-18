nums=list(map(int,input().split()))
k=int(input())
nums.sort()
n=len(nums)-(k+1)
print(nums[n])

# 8 4 6 2 3 5
# 2 3 4 5 6 8
# 2  -k
# greatest element after k iterations
# 5