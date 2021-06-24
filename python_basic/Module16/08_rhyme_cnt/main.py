umber_people = int(input('Введите количество человек: '))
list_player = list(range(1, umber_people + 1))
print(list_player)
count = int(input('До скольки считалка? '))
print(f'Значит выбывает каждый {count} человек\n')
temp = -1

while len(list_player) != 1:
    print('Текущий круг людей', list_player)
    print('Начало счёта с номера', end=' ')
    print(list_player[temp+1] if temp != len(list_player)-1 else list_player[0])

    for num in range(count):
        if temp == len(list_player)-1:
            temp = -1
        temp += 1
    print('Выбывает человек под номером', list_player.pop(temp), '\n')
    temp -= 1
print('Остался человек под номером', list_player[0])
