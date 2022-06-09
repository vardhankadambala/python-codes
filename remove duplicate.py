a=[11,11,11,21,43,43,60]
b=[]
#print(b)
for i in range(len(a)):
    if i not in b:
        b.append(a[i])
print(*b)