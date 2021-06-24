nick_name = input('Введите ваше имя: ')
while True:
    action = input('Введите\n'
                   '1 если посмотреть чат\n'
                   '2 если оставить сообщение: ')
    if action == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                data = file.readlines()
                print(''.join(data))
        except FileNotFoundError:
            print('Ещё нет никаких сообщений.')
    elif action == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write('{}: {}\n'.format(nick_name, new_message))
    else:
        print('Введена неизвестная команда.')
