def sum_numeral(x):
    return sum(map(int, [item for item in x]))


n = input('Введите целое положительное число: ')
print()

sum_num = sum_numeral(n)
count_num = len(n)

print('Сумма цифр:', sum_num)
print('Кол-во цифр в числе:', count_num)
print('Разность суммы и кол-ва цифр:', sum_num - count_num)
