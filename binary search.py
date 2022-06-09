def bs(a, l, u, k):
    m = (l + u) // 2
    x = -1
    if a[m] == k:
        return m
    elif a[m] < k:
        x = bs(a, m+1, u, k)
    elif a[m] > k:
        x = bs(a, l,m-1, k)
    else:
        return x
    return x


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 10

print(bs(a, 0, len(a) - 1, k))
