text = input('Введите текст: ')
list_text = text.split()
max_sym = 0
ind_word = ''
for ind, elem in enumerate(list_text):
    if len(elem) > max_sym:
        max_sym = len(elem)
        ind_word = ind
print(list_text[ind_word])
print(max_sym)
