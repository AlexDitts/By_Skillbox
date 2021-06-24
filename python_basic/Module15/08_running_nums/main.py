n = int(input('Введите количество элементов списка: '))
shift = int(input('Сдвиг: '))
old_list = [int(input('Введите элемент списка: ')) for _ in range(n)]
new_max_index = n - shift
new_list = [old_list[item] for item in range(shift * -1, new_max_index)]
print(old_list)
print(new_list)
