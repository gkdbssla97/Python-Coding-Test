def only1func():
    val = 1
    n = int(input())
    while True:
        if val % n == 0:
            break
        else:
            val = val * 10 + 1
    return len(str(val))

while True:
    try:
        print(only1func())
    except:
        break