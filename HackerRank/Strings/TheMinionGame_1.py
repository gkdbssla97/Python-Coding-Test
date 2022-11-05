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

    idx = 0
    for x in string:
        if x[0] in jaum:
            STUART += len(string) - idx
            # print(STUART)
        else:
            KEVIN += len(string) - idx
            # print(KEVIN)
        idx += 1
    if KEVIN > STUART:
        print(f'Kevin {KEVIN}')
    elif KEVIN < STUART:
        print(f'Stuart {STUART}')
    else:
        print('Draw')
    # for x in str:


if __name__ == '__main__':
    s = input()
    minion_game(s)