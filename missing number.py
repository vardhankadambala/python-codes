n=int(input("Enter the sie of sequence"))
print("enter the numbers in the list")
l=list(map(int,input().split()))
s=n*(n+1)//2
print("the missing element is")
print(s-sum(l))