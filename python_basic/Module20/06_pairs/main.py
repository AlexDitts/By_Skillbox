import random

list_num = [random.randint(0, 100) for _ in range(10)]

print(list_num)

first_tuple = (list_num[num] for num in range(0, len(list_num), 2))
second_tuple = (list_num[num] for num in range(1, len(list_num), 2))
print(*zip(first_tuple, second_tuple))

first_list = []
second_list = []
[first_list.append(elem) if ind % 2 == 0 else second_list.append(elem) for ind, elem in enumerate(list_num)]
print(*zip(first_list, second_list))

dict_num = {}
{dict_num.setdefault(list_num[ind], list_num[ind + 1]) for ind in range(0, len(list_num), 2)}
print(*dict_num.items())
