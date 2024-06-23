def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=3, b=[1, 2, 3], c=25)
print_params(a=100)
print_params(b =25)
print_params(c=[1, 2, 3])


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print()

values_list = [5, 'строка', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print(print_params(*values_list))
print(print_params(**values_dict))

values_list2 = [54.32, "'строка'"]

print_params(*values_list2, 42)
