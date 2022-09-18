a = int(input())
b = a;
d = 0;
while a > 0:
    c = a % 10;
    d = d * 10 + c;
    a = a // 10

if d == b:
    print("palind")
else:
    print("not palindrome")