a=input()
b=a.replace(' ','')
c=b.replace(',','')
print(c)
if c==c[::-1]:
    print("Yes")
else:
    print("No")
