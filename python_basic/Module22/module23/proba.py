

for i in range(1, 10):
    a = int(input('Введите число: '))
    try:
        s = i/a
        print(s)
    except ZeroDivisionError:
        #print('Деление на ноль')
        pass



