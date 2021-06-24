n = int(input('Введите количество чисел: '))
num_list = [1 if num % 2 == 0 else num % 5 for num in range(n)]
print('Результат:', num_list)
