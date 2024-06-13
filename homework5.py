immutable_var = 'Сергей', 'Петрович', 'Никифоров', 1972, 'г.', 'р.'
tuple_ = immutable_var
print(tuple_)
#tuple_[0] = 'Пётр'
#print(tuple_) # TypeError: 'tuple' object does not support item assignment, элементы внутри кортежа не изменяются
mutable_list = ['Сергей', 'Петрович', 'Никифоров', 1972, 'г.', 'р.']
print(mutable_list)
mutable_list[0] = 'Пётр'
print(mutable_list)