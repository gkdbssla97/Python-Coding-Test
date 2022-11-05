from collections import deque

N, M = map(int, input().split())
patient = deque([(key, val) for key, val in enumerate(list(map(int, input().split())))])

cnt = 0
while True:
    cur = patient.popleft()
    if any(cur[1] < x[1] for x in patient):
        patient.append(cur)
    else:
        cnt += 1
        if cur[0] == M:
            break
print(cnt)

'''
5 2
60 50 70 80 90
'''

