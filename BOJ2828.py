N, M = map(int, input().split())
J = int(input())
apple = []

for _ in range(J):
    apple.append(int(input()))

move_cnt = 0
s = 1
e = M

for i in range(J):
    if s <= apple[i] <= e:
        continue
    elif e < apple[i]:
        move_cnt += apple[i] - e
        e = apple[i]
        s = e - (M - 1)
    elif s > apple[i]:
        move_cnt += s - apple[i]
        s = apple[i]
        e = s + (M - 1)
print(move_cnt)