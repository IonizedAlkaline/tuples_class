tuple1 = ("tuple", "a", 1)
print(tuple1)

int_tuple = (1, 2, 3)
print(int_tuple)

tuple_add = tuple1 + int_tuple
print(tuple_add)

tuple_repeat = (1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3)
print(tuple_repeat.count(1))

tuple_slicing = tuple_add[::2]
print(tuple_slicing)
