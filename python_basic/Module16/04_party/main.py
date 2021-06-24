def guest_came(x, y):
    if x >= 6:
        print(f'Извини, {y}, но мест нет\n')
    else:
        print(f'Привет, {y}\n')
        guests.append(y)


def guest_gone(y):
    if name_guest in guests:
        print(f'Пока, {y}')
        guests.remove(y)
    else:
        print('Такого гостя не было\n')


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
door = ''
while True:
    count_guests = len(guests)
    print(f'Сейчас на вечеринке {count_guests} человек:', guests)
    door = input('Гость пришёл или ушёл? ')
    if door == 'Пора спать':
        break
    name_guest = input('Имя гостя: ')
    if door == 'пришёл':
        guest_came(count_guests, name_guest)
    elif door == 'ушёл':
        guest_gone(name_guest)
print('Все легли спать')
