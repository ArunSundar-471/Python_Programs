def replace(ch1,ch2,n,s):
    for i in s:
        if(ch1==i):
            i = ch2
        elif(ch2==i):
            i=ch1
        print(i,end='')


s=input()
ch1=input()
ch2=input()
n=len(s)
replace(ch1,ch2,n,s)
