def ssort(a):
    l = []
    m = []
    # for i in range(len(a)):
    while len(a) != 0:
        if len(l) == 0:
            c = a.pop()
            l.append(c)
        elif l[-1] < a[-1]:
            c = a.pop()
            l.append(c)
        else:
            c = a.pop()
            for i in range(len(l)):
                d = l.pop()
                a.append(d)
            l.append(c)
        # print(a)
        print(l)

    return l


a = [25, 25, 16, 13, 4, 6, 9, 1]
# print(a.count(25))
#print(*a)
x = ssort(a)
print(*x)
