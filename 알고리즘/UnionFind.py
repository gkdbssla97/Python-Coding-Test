N = int(input())
val = [0] + list(map(int, input().split()))
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
        if val[v] >= val[w]:
            parent[v] = w
        else:
            parent[w] = v