class Property:

    def __init__(self, worth, divider=0):
        self.worth = worth
        self.divider = divider

    def tax_calc(self):
        return self.worth / self.divider


class Apartment(Property):

    def __init__(self, worth, divider=1000):
        super().__init__(worth, divider)


class Car(Property):

    def __init__(self, worth, divider=200):
        super().__init__(worth, divider)


class CountryHouse(Property):

    def __init__(self, worth, divider=500):
        super().__init__(worth, divider)


my_money = int(input('Сколько денег у Вас есть? '))
sum_tax = 0
print('Вводите стоимость перечисляемого имущества или ноль, если всё перечислили')
while True:
    cost = int(input('\nСтоимость имущества: '))
    tax = 0
    if cost == 0:
        break
    else:
        type_of_prop = int(input('Введите тип имущества   '
                                 '1 - Квартира   '
                                 '2 - Машина   '
                                 '3 - Дача: '))
        dict_of_prop = {1: Apartment(cost),
                        2: Car(cost),
                        3: CountryHouse(cost)}
        tax = dict_of_prop[type_of_prop].tax_calc()
        print(f'Сумма налога на данное имущество {tax}')
        sum_tax += tax
different = my_money - sum_tax
print(f'\nСумма всех налогов равна - {sum_tax}')
print(f'Вам не хватает {different}' if different < 0 else 'Вам хватает денег для уплаты налогов')
