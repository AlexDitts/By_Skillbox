def valid(check_str: str):
    list_fields = check_str.split()
    if len(list_fields) < 3:
        raise IndexError('НЕ присутствуют все три поля ')
    if not list_fields[0].isalpha():
        raise NameError('Поле имени содержит НЕ только буквы ')
    if '@' not in list_fields[1] or '.' not in list_fields[1]:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку) ')
    if list_fields[2] not in range(10, 100):
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99 ')


with open('registrations.txt', 'r', encoding='utf-8') as file:
    with open('registrations_good.log', 'w', encoding='utf-8') as good_log:
        with open('registrations_bad.log', 'w', encoding='utf-8') as bad_log:
            for person_data in file:
                try:
                    valid(person_data)
                except(ValueError, NameError, SyntaxError, IndexError) as err:
                    bad_log.write('В строке {} {}'.format(err, person_data))
                else:
                    good_log.write(person_data)
