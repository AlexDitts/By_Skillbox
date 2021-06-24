import random


def first_func(first_num, second_num):
    first_num += random.randint(0, 10)
    second_num += random.randint(0, 5)
    return first_num / second_num


def second_func(first_num, second_num):
    first_num -= random.randint(0, 10)
    second_num -= random.randint(0, 5)
    return second_num / first_num


with open('coordinates.txt', 'r') as file:
    with open('result.txt', 'w') as file_2:
        for line in file:
            nums_list = line.strip().split()
            try:
                num_func = 1
                res1 = first_func(int(nums_list[0]), int(nums_list[1]))
                num_func = 2
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(my_list))
            except ZeroDivisionError:
                print("Что-то пошло не так с {}-й функцией".format(num_func))
            except Exception:
                print("Что-то пошло не так : ")
