a = int(input())
b=a
i = 0
while a != 0:
    i = i * 10 + a % 10
    a = a // 10
if b==i:
    print("Yes")
else:
    print("No")