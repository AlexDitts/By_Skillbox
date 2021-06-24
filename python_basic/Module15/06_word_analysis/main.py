count = 0
word = input('Введите слово: ')
for symbol in word:
    if word.count(symbol) == 1:
        count += 1
print('Количество уникальных символов: ', count)
