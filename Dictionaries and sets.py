my_dict = {'Name': 'Ivan', 'Year_Of_Birth': 2002}
print(my_dict)
print(f'Existing value: {my_dict.get('Name')}{'\n'}Not existing value: {my_dict.get('City')}')
my_dict.update({'Second_Name': 'Chitakh',
                'City': 'Volzhskiy'})
deleted = my_dict.pop('Name')
print(deleted)
print(my_dict)

my_set = {10, 'Potato', 100.01, True, 10, 10, 100.01, True}
print(f'Set: {my_set}')
my_set.add(90), my_set.add('Chips')
my_set.remove(100.01)
print(f'Modified set: {my_set}')