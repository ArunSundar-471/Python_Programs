string = "big black bug bit bug big";


string = string.lower();


words = string.split(" ");
##print(string.split(" "))
#print(words);
#print(len(string))
for i in range(0,len(words)):
    count = 1;
    for j in range(i+1, len(words)):
        if(words[i]==(words[j])):
            count=count+1;
            words[j]="0";
    if(count>1 and words[i]!="0"):
        print(words[i]);



