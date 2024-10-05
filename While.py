my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
go = 0
while my_list[go] >= 0:
        if my_list[go] == 0:
                go += 1
                continue
        print(my_list[go])
        go += 1