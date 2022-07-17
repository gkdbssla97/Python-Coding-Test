steel = input()

stack = []

cnt = 0
# tmp = ''
# for x in steel:
#     if x == ')' and tmp != ')':
#         stack.pop()
#         cnt += len(stack)
#         print(f'#2:{cnt}')
#     elif x == '(':
#         stack.append(x)
#     elif x == ')' and tmp == ')':
#         stack.pop()
#         cnt += 1
#         print(f'#1:{cnt}')
#     tmp = x
for i in range(len(steel)):
    if steel[i] == '(':
        stack.append(steel[i])
    else:
        stack.pop()
        if steel[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)