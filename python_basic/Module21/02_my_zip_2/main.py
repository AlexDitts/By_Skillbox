def my_zip(*args):
    gen_of_gen = tuple(map(lambda gen: (elem for elem in gen), args))  # Я создал генератор генераторов.
    count = min(len(args[0]), len(args[1]))                            # почти как Генадий Генадьевич:)
    out_list = [(next(gen_of_gen[0]), next(gen_of_gen[1])) for _ in range(count)]
    return out_list


str_col = 'abcdefghijklmnop'
num_col = range(10)
dict_col = dict(zip(str_col, num_col))
print((my_zip(str_col, dict_col)))
print((my_zip(str_col, num_col)))

