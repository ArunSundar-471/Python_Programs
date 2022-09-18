def integers(m,n):
    l=[]
    t=[]
    for i in range(1,n+1):
        if(i%m==0):
            l.append(i)
        else:
            t.append(i)
    x=0
    y=0
    for i in l:
        x=x+i
    for i in t:
        y=y+i
    return (y-x)
m=int(input())
n=int(input())
print(integers(m,n))

# Arr: 3 2 1 7 5 4
#
# Output:
# 7
#
# Explanation
#
# The second largest element from the even position is 3.
# The second largest element from the odd position is 4.
# The output is 7 (3 + 4).