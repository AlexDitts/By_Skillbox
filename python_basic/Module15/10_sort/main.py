import random

old_list = [random.randint(0, 100) for elem in range(0, 20)]
print('Изначальный список:', old_list)
for item in range(len(old_list), 0, -1):
    for i in range(1, item):
        if old_list[i] < old_list[i - 1]:
            old_list[i], old_list[i - 1] = old_list[i - 1], old_list[i]
print('Отсортированный список:', old_list)
