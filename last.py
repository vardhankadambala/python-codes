l=[1,2,3,2,1]
b=[]
count=0
for i in range(len(l)-1,-1,-1):
    if l[i]==2:
        print(i)
        break