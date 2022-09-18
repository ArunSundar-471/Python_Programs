list1=list(map(int,input().split()))
#list2=[1,2,2,8,200]
list1_new=[]
for i in list1:
    if i not in list1_new:
        list1_new.append(i)
print(list1_new)

