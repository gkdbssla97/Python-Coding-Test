#card = [i for i in range(1, 21)]
card = list(range(21))
#print(card)
'''
for i in range(1, 11):
    ai, bi = map(int, input().split())
    tmp = ai - 1
    reverse_card = []
    for j in range(bi, ai - 1, -1):
        reverse_card.append(card[j - 1])
    #print(reverse_card)
    for k in range(len(reverse_card)):
        card[tmp] = reverse_card[k]
        tmp += 1
    #print(f'#{i + 1}: {card}')
print(card)
'''
for i in range(1, 11):
    ai, bi = map(int, input().split())
    #idx = 1
    # for k in range(ai, ((ai + bi) // 2) + 1):
    #     print(ai, (bi // 2) + 1, k)
    #     card[k - 1], card[bi - idx] = card[bi - idx], card[k - 1]
    #     idx += 1
    for j in range((bi - ai + 1) // 2):
        card[ai + j], card[bi - j] = card[bi - j], card[ai + j]
    print(f'#{i}: {card}')
        # 5 6 7 8 9 10
        # 4 5 6 7 8 9 - idx
    #print(f'#{i + 1}: {card}')
card.pop(0)
print(card)
'''
[19, 1, 2, 4, 3, 5, 8, 7, 6, 9, 15, 16, 17, 12, 11, 10, 14, 13, 18, 20]
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
'''