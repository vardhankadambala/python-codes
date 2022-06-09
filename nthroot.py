i = int(input())
for x in range(i):
    n, m = map(int, input().split())
    r = m ** (1 / n)
    r = "{:.6f}".format(r)
    print(r)
