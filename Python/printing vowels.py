text = input('Enter text: ')
l=[]
for char in text:
    if char.lower() in 'aeiou':
        l.append(char)
l.sort()
# print(*l)

s = ""
for x in l:
    s+=str(x)

print(s)
