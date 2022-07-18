calculator = input()

def priority(i):
    if i == '+' or i == '-':
        return 2
    elif i == '*' or i == '/':
        return 1
    else:
        return 0
stack = []
for i in calculator:
    if i == '(':
        stack.append(i)
    elif i.isdigit():
        print(i, end='')
    elif i == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end ='')
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(), end ='')
        stack.append(i)
while stack:
    print(stack.pop(), end='')

# 352*72-/+
# +/