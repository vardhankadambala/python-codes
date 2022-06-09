s=input()
l=[]
prev=None
for i in s:
    if prev!=i:
        l.append(i)
        prev=i
print(''.join(l))