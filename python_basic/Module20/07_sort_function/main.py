def sort_tuple(some_tuple):
    for elem in some_tuple:
        if type(elem) is not int:
            return some_tuple
    else:
        return tuple(sorted(some_tuple))


my_tuple = (2, 3, 6, 8, 5, 4, 8, 7)
your_tuple = (3.5, 3, 5, 7.5, 8, 2, 10)
print(sort_tuple(my_tuple))
print(sort_tuple(your_tuple))
