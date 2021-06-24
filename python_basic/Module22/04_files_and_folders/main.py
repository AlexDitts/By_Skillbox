import os


def view_cat(our_path, size_cat=0, subcat=0, file=0):
    for item in os.listdir(our_path):
        path = os.path.join(os.path.sep, our_path, item)
        if os.path.isdir(path):
            subcat += 1
            size_cat, subcat, file = view_cat(path, size_cat, subcat, file)
        elif os.path.isfile(path):
            size_cat += os.path.getsize(path)
            file += 1
    return round(size_cat/1024, 6), subcat, file


in_path = tuple(input('Введите путь до каталога через пробел: ').split())
abs_path = os.path.join(os.sep, *in_path)
print(abs_path)
print('Размер каталога: {}\n'
      'Количество подкаталогов: {}\n'
      'Количество файлов: {}'.format(*view_cat(abs_path)))
