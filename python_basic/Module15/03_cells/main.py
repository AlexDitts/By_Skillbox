count = int(input('Введите количество клеток: '))
cells = []
for item in range(count):
    element = (int(input(f'Эффективность {item+1} клетки:')))
    if item > element:
        cells.append(element)
print('Неподходящие значения:', *cells)
