def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 9, b = 2)
print_params(b = 'линия', c = False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1, 'стол', 'name']
values_dict = {'a': 3, 'b': 'окно', 'c': 'user'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [56, 'я устал']

print_params(values_list_2, 42)





