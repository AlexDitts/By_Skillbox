text = input('Введите строку: ')
count_sym = 1
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count_sym += 1
    elif text[i] != text[i + 1]:
        print(text[i] + str(count_sym), end='')
        count_sym = 1
print(text[-1] + str(count_sym), end='')
