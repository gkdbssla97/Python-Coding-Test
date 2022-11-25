def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False

    return False

phone_book = ["119", "97674223", "1195524421","4444"]
# print(min(phone_book))

print(solution(phone_book))