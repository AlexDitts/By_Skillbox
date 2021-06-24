def find(contact: str):                              # Поиск абонента в телефонной книге
    for subscriber in phone_book:                    # по фамилии
        if contact in subscriber:
            print(*subscriber, phone_book[subscriber])


def add(human_data: tuple, number: str):              # Добавление абонента
    if human_data in phone_book:                      # в телефонную книгу
        print('Такой контакт уже есть')
    else:
        phone_book.setdefault(human_data, number)
        print('Абонент успешно добавлен в телефонный справочник')


phone_book = {}

while True:
    action = input('Добавить/Найти: ').title()
    if action == 'Добавить':
        add(tuple(input('Введите имя и фамилию: ').title().split()),
            input('Введите номер телефона: ')
            )
    elif action == 'Найти':
        find(input('Введите фамилию: ').capitalize())
