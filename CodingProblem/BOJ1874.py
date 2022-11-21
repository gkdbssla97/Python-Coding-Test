from collections import deque

N = int(input())

arr = []
say = []
cur = 1
flag = 0
for _ in range(N):
    num = int(input())
    while cur <= num:
        arr.append(cur)
        say.append("+")
        cur += 1
    if arr[-1] == num:
        arr.pop()
        say.append("-")
    else:
        flag = 1
        print("NO")
        break
if flag == 0:
    for x in say:
        print(x)
