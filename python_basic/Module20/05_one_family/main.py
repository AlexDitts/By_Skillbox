data_base = {('Иванович', 'Андрей'): 26,
             ('Иванов', 'Андрей'): 26,
             ('Иванова', 'Елена'): 25,
             ('Иванов', 'Алексей'): 6,
             ('Петров', 'Михаил'): 30,
             ('Петрова', 'Анна'): 28,
             ('Петрова', 'Юлия'): 8
             }

surname = input('Введите фамилию: ').title()
tuple_of_options = (surname,)

if surname[-1] == 'а':
    tuple_of_options += (surname[:-1],)
else:
    tuple_of_options += surname + 'а',

for key, value in data_base:
    if key in tuple_of_options:                     # Не сразу допёр, что вхождение в кортеж
        print(key, value, data_base[key, value])    # и вхождение в строку - это разные вещи
