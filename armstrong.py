a = int(input())
b = a
l = []
i = 0
while a != 0:
    c = a % 10
    l.append(c)
    a = a // 10
for i in range(len(l)):
    l[i] = (l[i]) ** 3
e=sum(l)
if e==b:
    print("Yes Armstrong number")
else:
    print("Not Armstrong number")