#1
with open('names.txt', 'w') as file:
    file.write('alex\n')
    file.write('li\n')
    file.write('john\n')
    file.write('po\n')
    file.write('iten\n')

with open('names.txt') as file:
    line_count = 0
    for name in file:
        line_count += 1
        print(name.strip())
        try:
            if len(name.strip()) < 3:
                raise BaseException
        except BaseException:
            with open('log_errors.txt', 'a') as log_file:
                log_file.write(('The name {1} in {0} string is too short.\n'.format(line_count, name.strip())))

#2
import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


file = open('coordinates.txt', 'r')
for line in file:
    nums_list = line.strip().split()
    try:
        num_func = 1
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        num_func = 2
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        number = random.randint(0, 100)
        file_2 = open('result.txt', 'w')
        my_list = sorted([res1, res2, number])
        file_2.write(' '.join(my_list))
    except ZeroDivisionError:
        print("Что-то пошло не так с {}-й функцией".format(num_func))
    except Exception:
        print("Что-то пошло не так : ")
    finally:
file_2.close()
file.close()

#3
import random


def create_list_except():
    exceptions = []
    todo = set([BaseException])
    print(todo)
    while todo:
        ex = todo.pop()
        exceptions.append(ex)
        todo.update(ex.__subclasses__())
    raise random.choice(exceptions)


sum_num = 0
while sum_num <= 777:
    num = int(input('Введите число: '))
    sum_num += num
    if random.randint(1, 13) == 3:
        create_list_except()

#5


def calc(expression: str):
    first_num, action, second_num = tuple(expression.split())
    dict_option = {'+': int(first_num) + int(second_num),
                   '-': int(first_num) - int(second_num),
                   '*': int(first_num) * int(second_num),
                   '/': int(first_num) / int(second_num),
                   '//': int(first_num) // int(second_num),
                   '%': int(first_num) % int(second_num)
                   }
    return dict_option[action]


answer = 0
for i in range(10):
    s = input('Строка: ')
    try:
        current_calc = calc(s)
    except (ZeroDivisionError, TypeError, KeyError):
        continue
    answer += current_calc
print(answer)



#7

def calc(expression: str):
    first_num, action, second_num = tuple(expression.split())
    dict_option = {'+': int(first_num) + int(second_num),
                   '-': int(first_num) - int(second_num),
                   '*': int(first_num) * int(second_num),
                   '/': int(first_num) / int(second_num),
                   '//': int(first_num) // int(second_num),
                   '%': int(first_num) % int(second_num)
                   }
    return dict_option[action]


while True:
    answer = 0
    str_error = ''
    for i in range(2):
        s = input('Строка: ')
        try:
            current_calc = calc(s)
        except (ZeroDivisionError, TypeError, KeyError, ValueError):
            str_error = s
            continue
        answer += current_calc
    if str_error:
        correction = input('Обнаружена ошибка в строке {}. Хотите исправить? '.format(str_error))
        if correction.lower() != 'да':
            break
print(answer)




