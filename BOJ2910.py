N, C = map(int, input().split())

tmp = list(map(int, input().split()))
count = {} #dictionary
idx = 1
for s in tmp:
    if s in count:
        count[s][0] += 1
    else:
        count[s] = [1, idx]
        idx += 1
print(count)
numbers = [[i, j] for i, j in count.items()]
numbers.sort(key=lambda x:(-x[1][0], x[1][1]))
res = []
for i, j in numbers:
    res += [i] * j[0]
print(*res)