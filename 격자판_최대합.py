N = int(input())

cube = []
for i in range(N):
    cube.append(list(map(int, input().split())))

#행
max = 0
sum = 0
for i in range(N):
    sum = sum(cube[i])
    if sum > max:
        max = sum
print(max)


print(cube)

