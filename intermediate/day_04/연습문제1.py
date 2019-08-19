stack = [0] * 10
top = -1

# push
for i in range(3):
    stack[top + 1] = i
    top += 1

# pop
for i in range(3):
    t = stack[top]
    t -= 1
    print(t)