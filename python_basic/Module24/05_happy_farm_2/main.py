class Potato:
    states = {0: 'Отсутствует',
              1: 'Росток',
              2: 'Зелёная',
              3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def __str__(self):
        return f'Картошка № {self.index}'

    def is_ripe(self):
        if self.state >= 3:
            return True
        else:
            return False

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count+1)]

    def __str__(self):
        return 'Грядка'

    def grow_all(self):
        print('Картошка проростает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Вся картошка созрела')
            return True
        else:
            print('Картошка ещё не созрела')
            return False


class Gardner:

    def __init__(self, name='Mario', count=0):
        self.name = name
        self.take_potatoes = []
        self.gardens = None
        self.count = count

    def join_garden(self, unit):
        if isinstance(unit, PotatoGarden):
            self.gardens = unit
        else:
            raise TypeError('Этот метод для присоединения объектов класса "PotatoGarden')

    def to_water(self):
        print('Поливаем и пропалываем картошку')
        self.gardens.grow_all()

    def harvest(self):
        if self.gardens.are_all_ripe():
            print('Картошка созрела, пора собирать')
            while self.gardens.potatoes:
                self.take_potatoes.append(self.gardens.potatoes.pop(0))
                self.count += 1
            print(f'Садовник {self.name} собрал {self.count} мешков картошки')
        else:
            print('Собирать ещё рано')


cheerful_gardener = Gardner()
my_garden = PotatoGarden(5)
cheerful_gardener.join_garden(my_garden)
cheerful_gardener.to_water()
cheerful_gardener.harvest()
cheerful_gardener.to_water()
cheerful_gardener.harvest()
cheerful_gardener.to_water()
cheerful_gardener.harvest()
