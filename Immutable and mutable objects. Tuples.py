immutable_var = 1, 2, [3, 4], True, 'six'
print(immutable_var)
# immutable_var[0] = 0
# print(immutable_var)
# Нельзя изменять кортежи, они являются неизменяемым типом данных
mutable_list = [1, 2, [3, 4], True, 'six']
mutable_list[1] = 100000
print(mutable_list)