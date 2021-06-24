a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))
print('Года от', a, 'до', b, 'с тремя одинаковыми цифрами:')

for years in range(a, b+1):
    str_year = str(years)
    for item in str_year:
        if str_year.count(item) == 3:
            print(years)
            break
