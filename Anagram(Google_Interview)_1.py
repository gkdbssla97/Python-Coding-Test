from collections import deque

a = input()
b = input()
str = dict()

for x in a:
    str[x] = str.get(x, 0) + 1
for x in b:
    str[x] = str.get(x, 0) - 1
for x in a:
    print(str.get(x))
    if str.get(x) != 0:
        print("NO")
        break
else:
    print("YES")



'''
AbaAeCe
baeeACA
'''