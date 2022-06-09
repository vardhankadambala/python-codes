l=[]
for i in range(1000):
    a=int(input())
    if a==1:
        b=int(input())
        l.insert(0,b)
    elif a==2:
        b=int(input())
        l.append(b)
    elif a==3:
        c = int(input())
        b=int(input())
        l.insert(c-1,b)
    elif a==4:
        print(*l)
    elif a==5:
        exit()
    else:
        print("Wrong choice")