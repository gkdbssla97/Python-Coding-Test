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
for idx in calculator:
    if idx.isdigit():
        stack.append(idx)
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(cal(idx, int(a), int(b)))

print(stack[-1])

