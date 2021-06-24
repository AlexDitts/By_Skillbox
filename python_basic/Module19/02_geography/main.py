count_country = int(input('Введите количество стран: '))
list_country = [input(f'{i_country} страна: ').split() for i_country in range(1, count_country+1)]
dict_city = {country.pop(0): country for country in list_country}

for num in range(1, 4):
    city = input(f'Введите {num} город: ')
    for i_country, l_city in dict_city.items():
        if city in l_city:
            print(f'Город {city} расположен в стране {i_country}')
            break
    else:
        print(f'Данных по городу {city} нет')
