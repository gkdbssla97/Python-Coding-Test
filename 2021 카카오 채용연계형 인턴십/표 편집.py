from collections import deque

### 리스트로 풀기 실패

n = int(input())
k = int(input())
#cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
#arr = ["무지", "콘", "어피치", "제이지", "프로도", "네오", "튜브", "라이언"]
arr = [i for i in range(n)]
OX = ['O' for _ in range(n)]
#print(OX)
recover = dict()
#recover = []
for i in cmd:
    arr1 = list(recover)
    if i[0] == 'D':
        if k == len(arr) - 1:
            k = 0
        k += int(i[2])
    elif i[0] == 'U':
        if k == 0:
            k = len(arr)
        k -= int(i[2])
    elif i[0] == 'C':
        recover[k] = arr[k]
        arr.remove(arr[k])
        if k == len(arr):
            k -= 1
    elif i[0] == 'Z':
        # print(arr1)
        arr.insert(arr1[-1], arr1[-1])
        if arr1[-1] < k:
            k += 1
        del(recover[arr1[-1]])
        arr1.pop()
    # print(f'k:{k}, {arr[k]}')
    # print(recover)
    # print(arr)
    # print(OX)

tmp = []
for i in recover.keys():
    tmp.append(i)
#print(tmp)
while len(tmp) != 0:
    #print(len(OX), len(arr1))
    OX[tmp.pop()] = 'X'
    #arr1.pop()

ans = ''
for i in OX:
    ans += i
print(ans)
'''
8
2
D 2
C 
U 3
C
D 4
C
U 2
Z
Z    
'''