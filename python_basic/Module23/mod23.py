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


answer = 0

with open('calc.txt') as file:
    dict_example = {i: j for i, j in enumerate(file)}
    for example in dict_example:
        try:
            current_calc = calc(dict_example[example])
        except (ZeroDivisionError, TypeError, KeyError):
            continue
        answer += current_calc
    print(answer)
