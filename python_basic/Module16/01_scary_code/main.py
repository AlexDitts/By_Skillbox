main_list = [1, 5, 3]
first_add = [1, 5, 1, 5]
second_add = [1, 3, 1, 5, 3, 3]
main_list.extend(first_add)
num_5 = main_list.count(5)
while main_list.count(5) != 0:
    main_list.remove(5)
main_list.extend(second_add)
num_3 = main_list.count(3)
print('Кол-во цифр 5 при первом объединении:', num_5)
print('Кол-во цифр 3 при втором объединении:', num_3)
print(main_list)
