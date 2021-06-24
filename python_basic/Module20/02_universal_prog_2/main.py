def prime_elem(iter_col) -> list:
    return [iter_col[i] for i in is_prime(len(iter_col))]


def is_prime(num: int) -> tuple:
    temp = (2,)
    for ind in range(3, num, 2):
        for min_div in range(3, int(ind**0.5), 2):
            if ind % min_div == 0:
                break
        else:                   # совсем без else не получилось,
            temp += (ind,)      # но функция стала значительно проще и быстрее
    return temp                 # проверил вроде работает


test_str = 'abcdefghijklmnop'
test_list = list(range(31))
test_tuple = tuple(range(31))
test_dict = {i: i + 1 for i in range(31)}

print(prime_elem(test_str))
print(prime_elem(test_list))
print(prime_elem(test_tuple))
print(prime_elem(test_dict))
