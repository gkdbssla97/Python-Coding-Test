C, N = map(int, input().split())

def dfs(Level, sum):
    global max
    if N == Level:
        if C > sum and max < sum:
            max = sum
    else:
        dfs(Level + 1, sum)
        dfs(Level + 1, sum + pet[Level])
pet = []

for _ in range(N):
    pet.append(int(input()))

max = 0
dfs(0, 0)
print(max)
