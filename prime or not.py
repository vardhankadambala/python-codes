a=int(input())
temp=0
for i in range(2,a//2):
    if a%i==0:
      temp=temp+1
      break
if temp==1:
    print("Composite number")
else:
    print("prime")