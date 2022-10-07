from collections import deque
N = int(input())
natural = list(map(int, input().split()))

natural = deque(natural)
pick = res = []
cnt = 0
while True:
    if not pick:
        if natural[0] < natural[-1]:
            res += 'L'
            pick.append(natural.popleft())
        else:
            res += 'R'
            pick.append(natural.pop())
    else:
        if pick[-1] < natural[0] and pick[-1] < natural[-1]:
            if natural[0] < natural[-1]:
                res += 'L'
                pick.append(natural.popleft())
            elif natural[0] > natural[-1]:
                res += 'R'
                pick.append(natural.pop())
        elif natural[-1] < pick[-1] < natural[0]:
            res += 'L'
            pick.append(natural.popleft())
        elif natural[0] < pick[-1] < natural[-1]:
            res += 'R'
            pick.append(natural.pop())
        elif len(natural) == 1 and natural[0] > pick[-1]:
            res += 'L'
            pick.append(natural.popleft())
        else:
            break
for idx in res:
    if idx == 'L' or idx == 'R':
        print(idx, end ='')
'''
5
2 4 5 1 3
'''