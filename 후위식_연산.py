def cal(i, a, b):
    if i == '+':
        return a + b
    elif i == '-':
        return b - a
    elif i == '*':
        return a * b
    elif i == '/':
        return b / a
calculator = input()

stack = []
for i in calculator:
    if i.isdigit():
        stack.append(i)
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(cal(i, int(a), int(b)))

print(stack[-1])

