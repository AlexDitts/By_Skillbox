import os


def save_text(text):
    while True:
        save_path = os.path.join(*(input('Введите путь сохранения через пробел: ').split()))
        save_path = os.path.join(os.path.sep, save_path)
        if os.path.exists(os.path.join(save_path)):
            break
    while True:
        file_name = input('Введите название файла: ')
        option = 'w'
        if file_name in os.listdir(save_path):
            option = input('''Такой файл уже существует, нажмите 
            w - если перезаписать файл
            a - если дописать файл,
            0 - если записать в другой файл: ''')
            if option != '0':
                break
        else:
            break

    with open(os.path.join(save_path, file_name), f'{option}') as file:
        file.write(text)

    print('Файл успешно сохранён.')
    print()
    print('Содержимое файла: ')
    with open(os.path.join(save_path, file_name)) as file:
        print(file.read())


text = input('Введите текст: ')
save_text(text)
