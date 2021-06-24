from collections import Counter

text = input('Введите текст: ')
count_sym = dict(Counter(text))
print('Оригинальный словарь частот:')
for key, value in count_sym.items():
    print(f'{key}: {value}')
new_dict = {}
for frequency in set(count_sym.values()):
    new_dict[frequency] = []
    for key in count_sym:
        if count_sym.get(key) == frequency:
            new_dict[frequency].append(key)
print('Инвертированнвй словарь частот:')
for sym in new_dict:
    print(f'{sym}: {new_dict[sym]}')
