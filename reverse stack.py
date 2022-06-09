def sreverse(a):
    l = []
    for i in range(len(a)):
        b = a.pop()
        l.append(b)
    return l


a = list(map(int, input().split()))
c = sreverse(a)
print(*c)
