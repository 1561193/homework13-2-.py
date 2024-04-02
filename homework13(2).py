def print_params(a = 1, b = 'power', c = False):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])


vaiues_list = (False, 'str', 7)
values_dict = {'a': 1, 'b': 'power', 'c': True}
print_params(vaiues_list, values_dict )
print_params(*vaiues_list)
print_params(**values_dict )

values_list2 = ('str', True)
print_params(*values_list2, 42)




