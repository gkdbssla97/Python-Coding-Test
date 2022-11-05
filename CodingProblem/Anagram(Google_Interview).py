from collections import deque

a = list(input())
b = list(input())
a.sort()
b.sort()
if a == b:
    print("YES")
else:
    print("NO")


'''
AbaAeCe
baeeACA
'''