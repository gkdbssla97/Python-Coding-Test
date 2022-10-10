from collections import deque

### 리스트로 풀기 실패
n = int(input())
k = int(input())
#cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
cmd = ["D 2", "C"]
#arr = ["무지", "콘", "어피치", "제이지", "프로도", "네오", "튜브", "라이언"]
linked_list = {i: [i - 1, i + 1] for i in range(0, n)}
linked_list[0] = [None, 1]
linked_list[n - 1] = [n - 2, None]
print(linked_list)
OX = ['O' for _ in range(n)]
stack = []

for c in cmd:
    if c[0] == 'D':
        for _ in range(int(c[2:])): # D 2
            k = linked_list[k][1]
            print('D')
    elif c[0] == 'U':
        for _ in range(int(c[2:])):
            k = linked_list[k][0]
    elif c[0] == 'C':
        prev, next = linked_list[k]
        stack.append([prev, next, k])
        OX[k] = "X"
        print('C')
        if next == None:
            k = linked_list[k][0]
        else:
            k = linked_list[k][1]
        if prev == None:
            linked_list[next][0] = None
        elif next == None:
            linked_list[prev][1] = None
        else:
            linked_list[prev][1] = next
            linked_list[next][0] = prev
    elif c[0] == 'Z':
        prev, next, val = stack.pop()
        OX[val] = 'O'
        if prev == None:
            linked_list[next][0] = val
        elif next == None:
            linked_list[prev][1] = val
        else:
            linked_list[prev][1] = val
            linked_list[next][0] = val

