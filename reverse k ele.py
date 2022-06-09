
l=[1,2,3,4,5,6]
k=int(input())
n=len(l)
c=n//k
a=[]
start=0
end=k
i=0
while i<c:
    l[start:end] = l[start:end][::-1]
    start=end
    end=end+end
    i=i+1
print(*l)