def number_revers(x):
    point = x.find('.')
    return x[point-1::-1] + '.' + x[:point:-1]


n = input('Введите вещественное число: ')
k = input('Введите вещественное число: ')

revers_n = number_revers(n)
revers_k = number_revers(k)

print('Первое число наоборот:', revers_n)
print('Второе число наоборот:', revers_k)
print('Сумма чисел равна:', float(revers_n) + float(revers_k))
