from collections import deque

N, M = map(int, input().split())
patient = list(map(int, input().split()))
num = list(range(N))
res = patient[M]

cnt = 0
print(patient[M])
patient = deque(patient)
num = deque(num)
while patient:
    max_val = max(patient)
    #print(f'1:{patient} {num}')
    while patient and patient[0] < max_val:
        #print(f'2:{patient} {num}')
        patient.append(patient.popleft())
        num.append(num.popleft())
        #print(f'3:{patient} {num}')
    if patient.popleft() and num.popleft() == M:
        cnt += 1
        break
    cnt += 1
    #print(cnt)
print(cnt)


'''
5 2
60 50 70 80 90
'''

