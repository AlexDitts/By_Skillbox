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
    for example in file:
        try:
            current_calc = calc(example)
        except (ZeroDivisionError, TypeError, KeyError):
            continue
        answer += current_calc
    print(answer)
