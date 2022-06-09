a=0
b=1
k=int(input())
for i in range(k):
    if i<=1:
        result=i
    else:
        result=a+b
        a=b
        b=result
    print(result)
