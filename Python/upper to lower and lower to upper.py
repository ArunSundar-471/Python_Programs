# s="HackerRank"
def interchange(s):

 for i in s:
    if(i == i.lower()):
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')
    # print(i,end='')
s=input()
interchange(s)