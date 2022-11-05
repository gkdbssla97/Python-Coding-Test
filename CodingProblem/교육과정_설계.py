from collections import deque

essential = deque(input())
N = int(input())


for idx in range(N):
    idx = 0
    subject = deque(input())
    for x in subject:
        if x == essential[idx]:
            idx += 1
        elif x in essential:
            print(f'#{idx + 1} NO')
            break
        if idx == len(essential):
            print(f'#{idx + 1} YES')
            break
'''
CBA
3
CBDAGE
FGCDAB
CTSBDEA
'''