from collections import Counter

def check(s1, s2):

    if (Counter(s1) == Counter(s2)):
        #l-1 i-1 s-1 t-1 e -1 n-1 ---s1
        #s-1 i-1 l-1 e-1 n-1 t-1 ----s2
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

s1 = "listen"
s2 = "silent"
check(s1, s2)