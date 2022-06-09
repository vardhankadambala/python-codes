l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
l3=[]
n=len(l)
m=len(l1)
for i in range(n):
    a=l[i]*10**(n-i-1)
    #print(a)
    l2.append(a)
for i in range(m):
    a=l1[i]*10**(m-i-1)
    l3.append(a)
print("sum of two lists:",sum(l2)+sum(l3))