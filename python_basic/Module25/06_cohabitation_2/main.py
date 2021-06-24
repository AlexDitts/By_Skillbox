# Не разобрался, почему в некоторых случаях выводится информация об объекте, а не его имя
# Не проверял ещё персонажей на жив или мёртв
# Можно было бы обойтись классом Resident, не создавая класс House, но посчитал что слишком много
# будет атрибутов, плохо читается.
# По процессу игры есть мысли создать список параметров героев, каждый день сортировать их, какой параметр
# меньше, то действие и делать, но пока не знаю как


import random


class House:
    count_food = 0
    count_cat_food = 0
    count_money = 0

    def __init__(self, refrigerator=50, nightstand=100, food_for_cat=30, garbage=0):
        self.__refrigerator = refrigerator
        self.__nightstand = nightstand
        self.__food_for_cat = food_for_cat
        self.__garbage = garbage

    def get_refrigerator(self):
        return self.__refrigerator

    def get_nightstand(self):
        return self.__nightstand

    def get_food_for_cat(self):
        return self.__food_for_cat

    def get_garbage(self):
        return self.__garbage

    def set_refrigerator(self, refrigerator):
        self.__refrigerator += refrigerator
        if refrigerator < 0:
            House.count_food += abs(refrigerator)

    def set_nightstand(self, nightstand):
        self.__nightstand += nightstand
        if nightstand < 0:
            House.count_money += abs(nightstand)

    def set_food_for_cat(self, food_for_cat):
        self.__food_for_cat += food_for_cat
        if food_for_cat < 0:
            House.count_cat_food += abs(food_for_cat)

    def set_garbage(self, garbage):
        self.__garbage += garbage

    def next_day(self):
        self.set_garbage(10)


class Residents:
    list_resident = []

    def __init__(self, name, other, satiety):
        # TODO: Добавьте в качестве атрибута дом, в который записывайте экземпляр класса дома.
        #  Чтобы не передавать other в каждый метод, когда к дому можно обратиться через существо в нем живущее.
        self.__name = name
        self.__satiety = satiety if satiety < 100 else 100
        self.list_resident.append(self)
        self.other = other

    def get_satiety(self):
        return self.__satiety

    def get_name(self):
        return self.__name

    def set_satiety(self, satiety):
        self.__satiety += satiety

    def eat(self,):
        print(f'{self.get_name()} ест ')
        food = self.other.get_refrigerator()
        if 30 < food:
            self.set_satiety(30)
            self.other.set_refrigerator(-30)
        else:
            self.set_satiety(food)
            self.other.set_refrigerator(0)

    def check_satiety(self):
        if self.get_satiety() < 0:
            print(f'{self.get_name()} умер от голода')
            self.list_resident.remove(self.list_resident.index(self))


class People(Residents):
    def __init__(self, name, other, satiety, happy):
        super().__init__(name, other, satiety)
        self.__happy = happy

    def pet_the_cat(self):
        print(f'{self.get_name()} гладит кота ')
        self.set_happy(5)
        self.set_satiety(-10)

    def get_happy(self):
        return self.__happy

    def set_happy(self, happy):
        self.__happy += happy

    def check_mood(self):
        if self.get_happy() < 10:
            print(f'{self.other.get_name()} умер от депрессии')
            self.other.list_resident.remove(self.other.list_resident.index(self))


class Husband(People):

    def __init__(self, name, other, satiety, happy):
        super().__init__(name, other, satiety, happy)

    def work(self):
        print(f'{self.get_name()} работает')
        self.other.set_nightstand(150)
        self.set_satiety(-10)

    def game_comp(self):
        print(f'{self.get_name()} играет в видеоигры')
        self.set_happy(20)
        self.set_satiety(-10)

    def act(self):
        if self.other.get_nightstand() < 150:
            self.work()
        elif self.get_satiety() < 20:
            self.eat()
        else:
            self.game_comp()


class Wife(People):
    count_fur_coat = 0

    def __init__(self, name, other, satiety, happy):
        super().__init__(name, other, satiety, happy)

    def clean_the_house(self):
        print(f'{self.get_name()} убирается в доме')
        self.other.set_garbage(-self.other.get_garbage())
        self.set_satiety(-10)

    def buy_fur_coat(self):
        print(f'{self.get_name()} купила шубу')
        if self.other.get_nightstand() >= 350:
            self.other.set_nightstand(-350)
            self.set_happy(65)
            self.set_satiety(-10)
            self.count_fur_coat += 1
        else:
            pass

    def buy_food(self):
        print(self.get_name(), 'покупает продукты')
        self.set_satiety(-10)
        if 130 < self.other.get_nightstand():
            self.other.set_nightstand(-130)
            self.other.set_refrigerator(100)
            self.other.set_food_for_cat(30)
        else:
            self.other.set_refrigerator(round(self.other.get_nightstand * 0.7))
            self.other.set_food_for_cat(round(self.other.get_nightstand * 0.3))
            self.other.set_nightstand(-self.other.get_refrigerator() - self.other.get_food_for_cat())

    def act(self):
        if house.get_refrigerator() < 100 or house.get_food_for_cat() < 30:
            self.buy_food()
        elif self.get_satiety() < 20:
            self.eat()
        elif self.other.get_garbage() > 90:
            self.clean_the_house()
        elif self.other.get_nightstand() > 600:
            self.buy_fur_coat()
        else:
            self.pet_the_cat()


class Cat(Residents):
    def __init__(self, name, other, satiety):
        super().__init__(name, other, satiety)

    def eat(self):
        print(f'{self.get_name()} ест')
        food_for_cat = self.other.get_food_for_cat()
        if food_for_cat > 10:
            self.set_satiety(20)
            self.other.set_food_for_cat(-10)
        else:
            self.set_satiety(food_for_cat * 2)
            self.other.set_food_for_cat(-food_for_cat)

    def tear_wallpaper(self):
        self.set_satiety(-10)
        self.other.set_garbage(5)
        print(f'{self.get_name()} дерёт обои')

    def sleep(self):
        self.set_satiety(-10)
        print(f'{self.get_name()} спит')

    def act(self):
        if self.get_satiety() < 20:
            self.eat()
        else:
            self.tear_wallpaper()


house = House()
husband = Husband('Валера', house, 30, 100)
wife = Wife('Галя',house, 30, 100)
cat = Cat('Бегемот', house, 30)
day = 0
print(husband.get_name())
while day <= 365:
    for individual in Residents.list_resident:
        individual.act()
        individual.check_satiety()
        if 'get_happy' in individual.__dir__():
            individual.check_mood()
    house.next_day()
    day += 1

print(f'\nКуплено шуб: {wife.count_fur_coat}\n'
      f'Съедено еды: {house.count_food}\n'
      f'Кот съел корма: {house.count_cat_food}\n'
      f'Потрачено денег {house.count_money}')
