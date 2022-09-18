
nums=[1,5,2,1,4,5,1]
d=[x for x in nums if nums.count(x)>1]
print(*d)
print("\t")
s={x for x in nums if nums.count(x)>1}
print(*s)



