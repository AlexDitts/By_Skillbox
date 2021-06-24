import random
count_skate = int(input('Введите количество пар коньков: '))
count_men = int(input('Введите количество человек: '))
skate_size = []
men_size = []

for item in range(1, count_skate+1):                    # Создание списка размеров коньков
    skate_size.append(random.randint(38, 44))           # и вывод его на экран
    print(f'Размер {item} пары: {skate_size[item-1]}')

for foot in range(1, count_men+1):                      # Создание списка размеров ног людей
    men_size.append(random.randint(38, 43))             # и вывод его на экран
    print(f'Размер ноги {foot} человека: {men_size[foot-1]}')

count = 0
for men in sorted(men_size):
    for size in sorted(skate_size):
        if men <= size:
            count += 1
            skate_size.remove(size)
            break

print('Наибольшее количество людей которые могут взять коньки:', count)
