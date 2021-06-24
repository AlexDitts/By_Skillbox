# Условия немного подправил исходя из логики поведения персонажа
# Персонаж не может заиграться до смерти, ровно как и заработаться до смерти
# Персонаж не может съесть больше чем лежит в холодильнике
# Персонаж не может потратить больше денег чем есть в тумбочке
# Две единицы продукта стоят 1 единицу денег.

import random


class Person:

    def __init__(self, name, satiety=50, is_alive=True):
        house.list_of_residents.append(self)
        self.name = name
        self.satiety = satiety
        self.is_alive = is_alive
        if self.satiety < 0:
            self.death()

    def eat(self):
        print(f'Персонаж {self.name} ест')
        to_full_saturation = 100 - self.satiety
        if to_full_saturation < house.refrigerator:
            house.refrigerator -= to_full_saturation
            self.satiety += to_full_saturation
        else:
            self.satiety += house.refrigerator
            house.refrigerator -= house.refrigerator
        print(f'Сытость: {self.satiety}')
        print(f'Еды в холодильнике: {house.refrigerator}')
        if house.nightstand < 1:
            self.work()
        if house.refrigerator < 1:
            self.go_to_supermarket()

    def play(self):
        print(f'Персонаж {self.name} играет')
        if self.satiety > 40:
            self.satiety -= 30
        else:
            self.satiety -= (self.satiety - 10)

    def work(self):
        print(f'Персонаж {self.name} работает')
        if self.satiety > 71:
            house.nightstand += 140
            self.satiety -= 70
        else:
            house.nightstand += (self.satiety - 1) * 2
            self.satiety -= (self.satiety - 1)

    def go_to_supermarket(self):
        print(f'Персонаж {self.name} идёт в магазин')
        if house.nightstand > 100:
            house.refrigerator += 100
            house.nightstand -= 100
        else:
            house.refrigerator += house.nightstand
            house.nightstand -= house.nightstand
        print(print(f'Еды в холодильнике {house.refrigerator}'))

    def death(self):
        print(f'{house.list_of_residents.pop(house.list_of_residents.index(self)).name} умер от голода')
        return False

    def check_state(self):
        if self.satiety <= 0:
            self.death()

    def az_yez_life_my(self):       # что означает "Аз езьм житье мое"
        if self.satiety < 20:
            self.eat()
        elif house.refrigerator < 10:
            self.go_to_supermarket()
        elif house.nightstand < 50:
            self.work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        else:
            self.play()


class House:

    def __init__(self, nightstand=10, refrigerator=50):
        self.nightstand = nightstand
        self.refrigerator = refrigerator
        self.list_of_residents = []


house = House()
first_resident = Person('Bob')
second_resident = Person('Billy')
day = 365
print(house.list_of_residents)
while day > 0:
    print(f'Количество жильцов {len(house.list_of_residents)}')
    day -= 1
    dice = random.randint(1, 6)
    print(f'кубик выпал {dice}')
    for resident in house.list_of_residents:
        resident.az_yez_life_my()              # метод так метод
