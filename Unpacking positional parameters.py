def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
# print_params(a) Ошибка
# print_params(b) Ошибка
# print_params(c) Ошибка
print_params(a = 'spider')
print_params(a = 'strider', b = 10123)
print_params(a = ['gonzo', 9010, False], b = {1: 'Unbelivable', 2: 'Greatfull'}, c = 'Papa Carlo')
print_params(b = 25)
print_params(c = [1,2,3])


values_list = ['mask', 1.000001, False]
values_dict = {'a': 'No Problemo', 'b': False, 'c': 10000000000}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [10, 10.1]
print_params(*values_list_2, 42)