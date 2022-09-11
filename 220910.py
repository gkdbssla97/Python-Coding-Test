tuple_list = [('안녕', 0),
                   ('hi', 1),
                   ('hello', 3),
                   ('good_bye', 2),
                   ('good_morning', 5)]

tuple_list.sort(key=lambda x: (-x[1], x[0]))  # '-'부호를 이용해서 역순으로 가능
print(tuple_list)