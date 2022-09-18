
nums=list(map(int,input().split()))
l=[]
for i in nums:
 i=abs(i)
 if(nums[i]>0):nums[i]*=-1
 else: l.append(i)
print(*l)
