N = int(input())

top = [list(map(int, input().split())) for _ in range(N)]
move_x = [-1, 0, 1, 0] #λΆλλ¨μ
move_y = [0, 1, 0, -1]
cnt = 0
for i in range(N):
    val = []
    for j in range(N):
        for k in range(4):
            nx = i + move_x[k]
            ny = j + move_y[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                val.append(0)
            else:
                val.append(top[nx][ny])
        #print(val)
        if max(val) < top[i][j]:
            cnt += 1
        val.clear()

print(cnt)
'''
5
5 3 7 2 3 
3 7 1 6 1 
7 2 5 3 4 
4 3 6 4 1 
8 7 3 5 2
'''