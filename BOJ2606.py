N = int(input())
M = int(input())
computer = [[] for _ in range(N + 1)]
ch = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

#print(computer)
def dfs(v, cnt):
    #ch[v] = 1
    for i in computer[v]:
        #print(i)
        if ch[i] == 0:
            ch[i] = 1
            dfs(i, cnt + 1)


dfs(1, 0)
print(ch.count(1) - 1)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''