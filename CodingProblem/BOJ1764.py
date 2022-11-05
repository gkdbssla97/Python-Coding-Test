N, M = map(int, input().split())
person = {}
res = []
cnt = 0

for i in range(N):
    D = input()
    person[D] = 1
    #print(person.get(D))
for j in range(M):
    B = input()
    if person.get(B):
        res.append(B)
        cnt += 1
res.sort()
print(cnt)
for x in res:
    print(x)