import os
from collections import Counter


alphabet = tuple(map(chr, range(ord('a'), ord('z'))))
quantity_char = 0
min_char = ''
temp = 100
with open(os.path.join('..', '02_zen_of_python', 'zen.txt')) as my_file:
    text = my_file.read()
    print('Количество строк в тексте', len(text.splitlines()))
    print('Количество слов в тексте', len(text.split()))
    col_sym = Counter(text.lower())
    for char in alphabet:
        current_quant = col_sym[char]
        quantity_char += current_quant
        if 0 < current_quant < temp:
            temp = current_quant
            min_char = char
    print('Количество букв в тексте: ', quantity_char)
    print('Самая редкая буква: ', min_char)
