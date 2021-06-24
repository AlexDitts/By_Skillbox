n = int(input('Введите количество пар слов: '))
dict_syn = {}

for num in range(1, n+1):
    print(f'{num} пара: ', end='')
    temp = input().split(' - ')
    dict_syn[temp[0]] = temp[1]
    dict_syn[temp[1]] = temp[0]
print(dict_syn)

while True:
    word = input('Введите слово: ').title()
    if word in dict_syn:
        print('Синоним:', dict_syn[word])
        break
    else:
        print('Такого слова в словаре нет')
