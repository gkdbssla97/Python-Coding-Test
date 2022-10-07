str = input()
num = ""
for idx in str:
    #if i >= '0' and i <= '9':
    if idx.isdigit():
        num += idx
num = int(num)
print(num)
cnt = 0
for idx in range(1, num + 1):
    if num % idx == 0:
        cnt += 1
print(cnt)