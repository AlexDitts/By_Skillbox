#4
import os


def view_cat(our_path, size_cat=0, subcat=0, file=0):
    for item in os.listdir(our_path):
        path = os.path.join(our_path, item)
        if os.path.isdir(path):
            subcat += 1
            size_cat, subcat, file = view_cat(path, size_cat, subcat, file)
        elif os.path.isfile(path):
            size_cat += os.path.getsize(path)
            file += 1
    return size_cat, subcat, file


in_path = tuple(input('Введите путь до каталога через пробел: ').split())
abs_path = os.path.join(*in_path)
print(abs_path)
print(view_cat(abs_path))


#5
import os


def save_text(text):
    while True:
        save_path = os.path.join(*input('Введите путь сохранения через пробел: ').split())
        if os.path.exists(save_path):
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

#6
with open('text.txt', 'w') as file:
    file.write('hello\nhello\nhello\nhello\nhello\nhello')


trg_file = open('cipher_text.txt', 'w')     # В задании не сказано, что сообщения будут по несколько слов
with open('text.txt', 'r') as src_file:     # так бы ещё сплит пришлось сделать
    for num_str, i_str in enumerate(src_file):
        crypt_str = ''
        for sym in i_str.strip():
            crypt_str += chr((ord(sym) + (num_str + 1) - 97) % 26 + 97)
        trg_file.write(crypt_str)
trg_file.close()

#7
def short_name(my_list):
    my_list[0], my_list[1] = my_list[1][0] + '.', my_list[0]
    return my_list


with open('first_tour.txt') as file:
    frontier = file.readline()
    list_players = [player.split() for player in file if player.split()[2] > frontier]

list_players.sort(key=lambda x: x[2], reverse=True)
gen_players = list(map(short_name, list_players))

with open('second_tour.txt', 'w') as trg_file:

    trg_file.write(f'{str(len(gen_players))}\n')
    for num, player in enumerate(gen_players):
        trg_file.write('{0}) {1}\n'.format(num+1, ' '.join(player)))

print('Содержимое файла "second_tour.txt":')
with open('second_tour.txt') as new_file:
    print(new_file.read())

#8
import os

with open('file.txt', 'w') as file:
    file.write('Mama myla ramu')

with open('file.txt') as file:
    sym_dict = {}
    quant_char = 0
    for line in file:
        for sym in line:
            if sym.isalpha():
                quant_char += 1
                sym_dict.setdefault(sym, 0)
                sym_dict[sym] += 1

sym_tuple = sorted(sorted(sym_dict.items()), key=lambda para: para[1], reverse=True)

with open('analysis.txt', 'w') as file_trg:
    for couple in sym_tuple:
        file_trg.write('{} {:.3f}\n'.format(couple[0], couple[1]/quant_char))
print('Содержание файла "analysis.txt":')
with open('analysis.txt') as end_file:
    for _ in range(len(sym_tuple)):
        print(end_file.readline().strip())

