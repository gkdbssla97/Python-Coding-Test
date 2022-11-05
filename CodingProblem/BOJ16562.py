N, M, k = map(int, input().split())
friend_fee = [0] + list(map(int, input().split()))
parent = [i for i in range(N + 1)]

def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(v, w):
    v = find(v)
    w = find(w)
    if v != w:
        if friend_fee[v] >= friend_fee[w]:
            parent[v] = w
        else:
            parent[w] = v

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

total = 0
ch = set()
for i in range(1, N + 1):
     v = find(i)
     if v in ch:
         continue
     else:
         ch.add(v)
         total += friend_fee[v]
print(total if total <= k else "Oh no")