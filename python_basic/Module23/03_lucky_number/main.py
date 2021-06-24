import random


def create_list_except():
    exceptions = []
    set_except = {BaseException}
    print(set_except)
    while set_except:
        ex = set_except.pop()
        exceptions.append(ex)
        set_except.update(ex.__subclasses__())
    raise random.choice(exceptions)


with open('num.txt', 'w') as file:
    sum_num = 0
    while sum_num <= 777:
        num = int(input('Введите число: '))
        sum_num += num
        if random.randint(1, 13) == 3:
            create_list_except()
        file.write(str(num))
