text_in_file = '   2  \n   2     2  \n  5  3\n   7  \n'   # Создание файла для задания
with open('numbers.txt', 'w', encoding='utf-8') as my_file:
    my_file.write(text_in_file)

with open('numbers.txt', encoding='utf-8') as my_file:
    sum_num = 0
    for i_str in my_file:
        for num in i_str.strip():
            if num.isdigit():
                sum_num += int(num)
print(sum_num)
