N = int(input())

p = dict()
for idx in range(N):
    word = input()
    p[word] = 1
for idx in range(N - 1):
    word = input()
    p[word] = 0
print(p.items())
for key, val in p.items():
    if val == 1:
        print(key)
        break
'''
5
big
good
sky
blue
mouse
sky
good
mouse
big
'''