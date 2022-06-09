l=list(map(str,input().split()))
a,b=[],[]
v='AaEeIiOoUu'
for i in l:
    if i in v:
        a.append(i)
    else:
        b.append(i)
print(*a)
print(*b)
c=a+b
print(*c)