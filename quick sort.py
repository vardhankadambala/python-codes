def qsort(l):
    if l is None:
        return l
    else:
        p = l[-1]
        l.pop()
        l1 = []
        l2 = []
        for x in range(len(l)):
            if x < p:
                l1.append(x)
            else:
                l2.append(x)
        l3 = qsort(l1)
        l4 = qsort(l2)
        return l3 + p + l4


l = [9, 8, -1, 1, -6, 4, 2, 3]
print(qsort(l))
