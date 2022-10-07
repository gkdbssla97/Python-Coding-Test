N, M = map(int, input().split())
J = int(input())
apple = []

for _ in range(J):
    apple.append(int(input()))

move_cnt = 0
s = 1
e = M

for idx in range(J):
    if s <= apple[idx] <= e:
        continue
    elif e < apple[idx]:
        move_cnt += apple[idx] - e
        e = apple[idx]
        s = e - (M - 1)
    elif s > apple[idx]:
        move_cnt += s - apple[idx]
        s = apple[idx]
        e = s + (M - 1)
print(move_cnt)