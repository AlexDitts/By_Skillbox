import random
first_list = [random.randint(500, 1000) / 100 for _ in range(20)]
second_list = [random.randint(500, 1000) / 100 for _ in range(20)]
third_list = [i if i > j else j for i, j in zip(first_list, second_list)]
print('Первая команда:', first_list)
print('Вторая команда:', second_list)
print('Победители тура', third_list)
