from collections import deque
N = int(input())
natural = list(map(int, input().split()))

natural = deque(natural)
pick = res = []

lt = 0
rt = N - 1
last = 0

while lt <= rt:
    if last < natural[lt]:
        pick.append((natural[lt], "L"))
    if last < natural[rt]:
        pick.append((natural[rt], "R"))
    pick.sort()
    if len(pick) == 0:
        break
    else:
        res += pick[0][1]
        last = pick[0][0]
        if pick[0][1] == 'L':
            lt += 1
        else:
            rt += 1
    pick.clear()

'''
5
2 4 5 1 3
'''