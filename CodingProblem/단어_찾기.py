N = int(input())

word = []
comp = []
for idx in range(N):
    word.append(input())
for idx in range(N - 1):
    comp.append(input())

print(word)
print(comp)
for x in word[:]:
    if x in comp:
        word.remove(x)
print(word[0])
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