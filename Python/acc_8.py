def function(a,b,c):
    if(c==1):
        return a+b
    elif(c==2):
        return a-b
    elif(c==3):
        return a*b
    elif(c==4):
        return a//b


a=int(input())
b=int(input())
c=int(input())
print(function(a,b,c))

