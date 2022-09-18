
def funct(st1,st2):
  for i in range(len(st1)+1-len(st2)):
    if st1[i:i+len(st2)]==st2:
      return True
    else:
      return False
      break

st1=input()
st2=input()
print(funct(st1,st2))