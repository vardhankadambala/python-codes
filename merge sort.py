def msort(l1, l2, n1, n2):
    l3 = [None] * (n1 + n2)
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            l3[k] = l1[i]
            k = k + 1
            i = i + 1
        else:
            l3[k] = l2[j]
            k = k + 1
            j = j + 1
    while j < n2:
        l3[k] = l2[j]
        k = k + 1
        j = j + 1
    l3.sort()
    return l3


l1 = [36, 35]
l2 = [43, 12]
n1 = len(l1)
n2 = len(l2)
print("merge sort is", msort(l1, l2, n1, n2))
print("normal s", l1 + l2)
