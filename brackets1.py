s = input()
l = []
t = -1
k = '{[('
for i in s:
    if i in k:
        print(i)
        l.append(i)
        t += 1
    elif i == l[t]:
        l.pop()
        t -=1
        print(l)
    else:
        print(False)
        exit(0)
print(True)