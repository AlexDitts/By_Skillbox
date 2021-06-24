def find_key(struct, key, fdeep=None):
    if key in struct:
        return struct[key]
    if fdeep == 0:
        return 'Достигнута указанная глубина вложения'

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            if fdeep:
                result = find_key(sub_struct, key, fdeep=fdeep-1)
            else:
                result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Какой ключ ищем? ')
deep = int(input('До какой глубины? '))
value = find_key(site, user_key, fdeep=deep)
if value:
    print(value)
else:
    print('Такого ключа в словаре нет.')

