old_list = []
count = int(input('Количество видеокарт: '))
for item in range(count):
    card = int(input(f'{item+1} видеокарта: '))  # надеюсь версий Титаниум не будет в списке.
    old_list.append(card)
max_card = max(old_list)
new_list = old_list.copy()
while max_card in new_list:
    new_list.remove(max_card)
print('Старый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)
