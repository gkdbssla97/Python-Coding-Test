from collections import deque

N = int(input())
braket = input()
q = deque()

cnt = 0
res = 0
ch = [0] * N
for i in range(len(braket)):
    if braket[i] == '(':
        q.append(i)
    if braket[i] == ')':
        if q:
            ch[i] = ch[q[-1]] = 1
            q.pop()
for i in ch:
    if i == 1:
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 0
print(res)
