max_num = int(input('Введите максимальное число: '))
num_set = set(range(1, max_num + 1))
my_nums = set()

while len(num_set) > 1:
    select_num = input('Нужное число есть среди вот этих чисел: ')
    if select_num == 'Помогите!':
        break
    digit_set = set(map(int, select_num.split()))
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        num_set = num_set & digit_set
    elif answer == 'Нет':
        num_set = num_set - digit_set
print('Артём мог загадать следующие числа:', *num_set)
