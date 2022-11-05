L = int(input())
box = list(map(int, input().split()))
M = int(input())

box.sort(reverse=True)
print(box)
cnt = 1
while cnt <= M:
    box[box.index(max(box))] -= 1
    box[box.index(min(box))] += 1
    cnt += 1
print(box)
print(max(box) - min(box))
'''
10
69 42 68 76 40 87 14 65 76 81
50
'''