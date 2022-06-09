l=list(map(int,input().split()))
l1,l2,l3,l4=[],[],[],[]
for i in range(len(l)):
    if l[i]%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
for i in range(len(l1)):
    if l1[i]%5==0:
        l3.append(l1[i])
    else:
        l4.append(l1[i])
l3.sort(reverse=True)
l4.reverse()
l1=l3+l4
l=l1+l2
print(l)