s = "{[]}(){}"
d = {"{" : "}", "[" : "]", "(":")"}

stack = []
for i in s:
    if i in d.keys():
        stack.append(i)
    elif i in d.values():
        #print(*stack)
        #print(stack[-1])
        #print(i)
        if d[stack[-1]] == i:
            stack.pop()
        else:
            print("False")
            exit(0)

if len(stack) != 0:
    print("False")
    exit()
else:
    print("True")
