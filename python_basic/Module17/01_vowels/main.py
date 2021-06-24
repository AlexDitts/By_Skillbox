vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
text = input('Введите текст: ')
list_vowels = [symbol for symbol in text if symbol in vowels]
print('Список гласных букв:', list_vowels)
print('Длина списка:', len(list_vowels))
