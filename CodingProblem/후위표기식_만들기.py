calculator = input()

def priority(i):
    if i == '+' or i == '-':
        return 2
    elif i == '*' or i == '/':
        return 1
    else:
        return 0
stack = []
for idx in calculator:
    if idx == '(':
        stack.append(idx)
    elif idx.isdigit():
        print(idx, end='')
    elif idx == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    elif idx == '*' or idx == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end ='')
        stack.append(idx)
    elif idx == '+' or idx == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(), end ='')
        stack.append(idx)
while stack:
    print(stack.pop(), end='')

# 352*72-/+
# +/