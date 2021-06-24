import random
first_list = [random.randint(0, 7) for _ in range(3)]
second_list = [random.randint(0, 7) for _ in range(7)]
print('Первый список:', first_list)
print('Второй список', second_list)
first_list.extend(second_list)
print('Расширенный первый список', first_list)
for item in first_list:
    while first_list.count(item) > 1:  # Условный оператор не использован согласно условию задачи
        first_list.remove(item)
print('Изменённый первый список:', first_list)
