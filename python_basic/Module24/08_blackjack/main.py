import random


class Players:

    __deck = {'2 б': 2, '3 б': 3, '4 б': 4, '5 б': 5, '6 б': 6, '7 б': 7, '8 б': 8,
              '9 б': 9, '10 б': 10, 'Валет б': 10, 'Дама б': 10, 'Король б': 10, 'Туз б': 11,
              '2 ч': 2, '3 ч': 3, '4 ч': 4, '5 ч': 5, '6 ч': 6, '7 ч': 7, '8 ч': 8,
              '9 ч': 9, '10 ч': 10, 'Валет ч': 10, 'Дама ч': 10, 'Король ч': 10, 'Туз ч': 11,
              '2 к': 2, '3 к': 3, '4 к': 4, '5 к': 5, '6 к': 6, '7 к': 7, '8 к': 8,
              '9 к': 9, '10 к': 10, 'Валет к': 10, 'Дама к': 10, 'Король к': 10, 'Туз к': 11,
              '2 п': 2, '3 п': 3, '4 п': 4, '5б': 5, '6 п': 6, '7 п': 7, '8 п': 8,
              '9 п': 9, '10 п': 10, 'Валет п': 10, 'Дама п': 10, 'Король п': 10, 'Туз п': 11
              }

    list_key = list(__deck.keys())

    @classmethod
    def get_deck(cls) -> dict:
        return cls.__deck

    def __init__(self, name='', hand=0):
        self.name = name if name else 'Дилер'
        self.hand = hand
        self.cards = [self.list_key.pop(self.list_key.index(random.choice(self.list_key))) for _ in range(2)]  # Набираем карты
        score = sum([self.get_deck()[card] for card in self.cards])   # Считаем очки
        self.hand = score if score < 22 else score - 10         # Считаем с учётом туза
        print(self.name)
        print(f'Карты: {self.cards}   Очки: {self.hand}\n' if self.name != 'Дилер' else '\n')

    def more(self):
        new_card = self.list_key.pop(self.list_key.index(random.choice(self.list_key)))  # Ещё
        self.cards.append(new_card)
        if new_card in ['Туз б', 'Туз ч', 'Туз к', 'Туз п'] and self.hand + self.get_deck()[new_card] > 21:
            self.hand += 1
        else:
            self.hand += self.get_deck()[new_card]
        print(self.name)
        print(f'Карты {self.cards}    Очки:   {self.hand}\n')

    def show_cards(self, rival):
        if rival.hand < self.hand < 22:
            print(f'Победил {self.name}')
        elif self.hand < rival.hand:
            print(f'Победил {rival.name}')
        else:
            print('Ничья')


player = Players(input('Введите имя игрока: '))
com = Players()

option = 0
while option != 2:
    option = int(input('1 - Ещё?, 2 - Вскрываемся: '))
    if option == 1:
        player.more()
    else:
        player.show_cards(com)
if input('Показать карты дилера?'
         ' 1 - Да,'
         ' 2 - Нет: '
         ) == '1':
    print('\nУ нас джентельменам верят наслово.')
