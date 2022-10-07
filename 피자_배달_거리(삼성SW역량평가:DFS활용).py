N, M = map(int, input().split())
pizza = [list(map(int, input().split())) for _ in range(N)]

p_pizza = []
p_house = []

# 중복조합으로 피자집 M개 선출
for idx in range(N):
    for j in range(N):
        if pizza[idx][j] == 1:
            p_house.append((idx, j))
        elif pizza[idx][j] == 2:
            p_pizza.append((idx, j))

def pick_M(v, s):
    global res
    if v == M:
        sum = 0
        for x1, y1 in p_house:
            #print(x1, y1)
            min_val = 2147000000
            for j in ch:
                print(j)
                x2 = p_pizza[j][0]
                y2 = p_pizza[j][1]
                min_val = min(min_val, abs(x1 - x2) + abs(y1 - y2))
            sum += min_val
        if res > sum:
            res = sum
    else:
        for i in range(s, len(p_pizza)):
            ch[v] = i
            pick_M(v + 1, i + 1)

ch = [0] * M

res = 2147000000
pick_M(0, 0)
print(res)
'''
4 4
0 1 2 0
1 0 2 1
0 2 1 2
2 0 1 2
'''