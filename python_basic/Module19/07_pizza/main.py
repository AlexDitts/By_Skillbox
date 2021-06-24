quantity_order = int(input('Введите количество заказоа: '))
dict_customer = {}
for num in range(1, quantity_order + 1):
    order = input(f'{num} заказ: ').split()
    customer, pizza, quantity = order[0], order[1], order[2]
    dict_customer.setdefault(customer, {})
    dict_customer[customer].setdefault(pizza, 0)
    dict_customer[customer][pizza] += (int(quantity))

for name in sorted(dict_customer.keys()):
    print(name)
    for i_pizza in sorted(dict_customer[name].keys()):
        print(f'    {i_pizza}: {dict_customer[name][i_pizza]}')
