def anagram(s1,s2):
    if(sorted(s1) == sorted(s2)):
        print("Anagram")
    else:
        print("not anagram")


s1 = input("enter a value")
s2 = input("enter b value")
anagram(s1,s2)