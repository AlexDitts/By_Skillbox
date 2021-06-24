shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

part = input('Название детали: ')
count_part = 0
price_part = 0
for position in shop:
    if position.count(part) == 1:
        count_part += 1
        price_part += position[1]

print('Количество деталей:', count_part)
print('Общая стоимость:', price_part)
