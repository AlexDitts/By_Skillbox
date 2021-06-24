def slice_by_elem(iter_col, elem) -> tuple:
    start_ind = len(iter_col)
    finish_ind = len(iter_col)
    flag = False
    for ind, i_elem in enumerate(iter_col):
        if i_elem == elem:
            if not flag:
                start_ind = ind
                flag = True
            elif flag:
                finish_ind = ind
                break
    return iter_col[start_ind: finish_ind + 1]


first_test = tuple(range(31))
second_test = (1, 5, 6, 8, 7, 20, 3, 5, 6, 9, 8, 7, 20, 3, 6, 5, 4, 7, 8)
third_elem = tuple(range(19))
rand_elem = 20
print(slice_by_elem(first_test, rand_elem))
print(slice_by_elem(second_test, rand_elem))
print(slice_by_elem(third_elem, rand_elem))
