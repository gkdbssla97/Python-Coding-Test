N = int(input())

max_list = []
for idx in range(N):
    dice = list(map(int, input().split()))
    if dice[0] == dice[1] == dice[2]:
        print(1)
        #max_list.append(10000 + dice[0] * 1000)
    elif dice[0] != dice[1] != dice[2]:
        #max_list.append(max(dice) * 100)
        print(2)
    else:
        if dice[0] == dice[1] or dice[0] == dice[2]:
            max_list.append(1000 + dice[0] * 100)
        else:
            max_list.append(1000 + dice[1] * 100)

print(max(max_list))

'''
3
3 3 6 
2 2 2 
6 2 5
'''
'''
for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.sort()
    if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
        print(1)
    elif tmp[0] == tmp[1] or tmp[1] == tmp[2]:
        print(2)
    elif tmp[1] == tmp[2]:
        print(3)
    else:
        print(4)
    if money > max_val:
        max_val = money
'''