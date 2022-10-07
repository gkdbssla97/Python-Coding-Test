import sys

M = int(sys.stdin.readline())
bit = 0
for _ in range(M):
    tmp = sys.stdin.readline().split()
    if len(tmp) == 1:
        if tmp[0] == 'all':
            bit = (1 << 20) - 1
            print(bin(bit))
        else:
            bit = 0
    else:
        cmd, num = tmp[0], int(tmp[1]) - 1
        if cmd == 'add':
            bit |= (1 << num)
        elif cmd == 'remove':
            bit &= ~(1 << num)
        elif cmd == 'check':
            if bit & (1 << num):
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            bit = bit ^ (1 << num)

