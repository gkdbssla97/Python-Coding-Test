from collections import deque

M, N = map(int, input().split())
#M = str(M)
#M = list(M)
M = list(map(int, str(M)))
print(M)
#max_val = max(M)
cnt = 0
stack = []
i = 0

# while cnt != N:
#     #print(M[i], M[i + 1])
#     if M[i] < M[i+1]:
#         M.remove(M[i])
#         #print("!")
#         cnt += 1
#         i = 0
#     else:
#         i += 1
#     if i == len(M):
#         i -= 1
#     if i == len(M) - 1:
#         while cnt != N:
#             M.pop()
#             cnt += 1
#         break
#     #print(cnt)
# for i in M:
#     print(i, end = '')

for x in M:
    while stack and N > 0 and stack[-1] < x:
        stack.pop()
        N -= 1
    stack.append(x)
if N != 0:
    stack = stack[:-N]

for i in stack:
    print(i, end = '')
'''
5276823 3
'''