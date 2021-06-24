forbidden_sym = '@№$%^&*()'
required_str = ['.txt', '.docx']
file_name = input('Введите название файла: ')

if file_name[0] in forbidden_sym:
    print('Ошибка - файл начинается на один из специальных символов')
else:
    for ext in required_str:
        if file_name.endswith(ext):
            print('Файл назван верно')
            break
    else:
        print('Неверное расширение файла. Ожидалось .txt или .docx')
