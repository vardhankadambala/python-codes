s = "{[]}(){}("
op = ['{', '(', '[']
cl = ['}', ')', ']']
stack = []
for i in s:
    if i in op:
        stack.append(i)
    elif i in cl:
        idx = cl.index(i)
        ele = op[idx]
        if ele == stack[-1]:
            stack.pop()
        else:
            print("False")
            exit()

if len(stack) != 0:
    print("False")
    exit()
else:
    print("True")
