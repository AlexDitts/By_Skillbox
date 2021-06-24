def translation(text, shift, n):
    new_max_index = n - shift
    return ''.join([text[i_elem] for i_elem in range(shift * -1, new_max_index)])


first_text = input('Введите строку первую строку: ')
second_text = input('Введите строку вторую строку: ')
num_sym = len(second_text)

for item in range(num_sym):
    temp = translation(second_text, item, num_sym)
    if temp == first_text:
        print('Первая строка получается из второй со сдвигом', item)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
