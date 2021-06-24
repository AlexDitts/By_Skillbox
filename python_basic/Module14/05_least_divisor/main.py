def min_divider(x):
    for divider in range(2, x+1):
        if x % divider == 0:
            print('Наименьший делитель отличный от 1 равен: ', int(divider))
            break


number = int(input('Введите первое число: '))
min_divider(number)
