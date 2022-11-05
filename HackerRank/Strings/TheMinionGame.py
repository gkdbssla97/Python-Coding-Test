from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict


def minion_game(string):
    # str = 'BANANA'
    #       #input()
    STUART = 0
    KEVIN = 0

    moum = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    jaum = list(ascii_uppercase + ascii_lowercase)
    for x in jaum:
        if x in moum:
            jaum.remove(x)

    ch = {}
    for start in range(len(str)):
        for end in range(start + 1, len(str) + 1):
            compare = str[start:end]
            if compare in ch:
                if compare[0] in jaum:
                    ch[compare] += 1
                elif compare[0] in moum:
                    ch[compare] += 1
            else:
                ch[compare] = 1
    for x in ch.items():
        if x[0][0] in moum:
            KEVIN += x[1]
        else:
            STUART += x[1]
    if KEVIN > STUART:
        print(f'KEVIN {KEVIN}')
    else:
        print(f'STUART {STUART}')
    # for x in str:


if __name__ == '__main__':
    s = input()
    minion_game(s)