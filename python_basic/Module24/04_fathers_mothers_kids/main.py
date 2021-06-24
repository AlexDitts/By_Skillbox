class Parent:

    def __init__(self, name, age):
        if int(age) < 16 or int(age) > 60:
            raise ValueError('Не подходящий возраст родителя')
        self.name = name
        self.age = age
        self.list_child = []

    def parent_info(self):
        print(f'Меня зовут{self.name}\n'
              f'Мне {self.age} лет\n'
              f'У меня есть дети: {self.list_child}')

    def feed(self, unit):
        unit.hunger += 5

    def calm_down(self, unit):
        unit.calm -= 1
        print(f'{unit.name}:\n {Child.scale_of_calm[unit.calm]}')

    def add_kinder(self, other):
        if other.age + 16 <= self.age:
            self.list_child.append(other)
        else:
            raise ValueError('Неподходящий возраст для ребёнка')


class Child:
    scale_of_calm = {1: 'У меня всё хаясё',
                     2: 'Скоя мама пйидёт?',
                     3: 'Купи тюпа-тюп',
                     4: 'Не хатю пать',
                     5: 'Аааааааааааа'}

    def __init__(self, name, age, hunger, calm):
        self.name = name
        self.age = age
        self.hunger = hunger if hunger < 6 else 5
        if calm < 1:
            self.calm = 1
        elif calm > 5:
            self.calm = 5
        else:
            self.calm = calm
        print(f'{self.name}:\n {Child.scale_of_calm[self.calm]}')
        print('Я хочу есть' if self.hunger < 3 else '', end='')


mother = Parent('Мама Люба', 32)
kinder = Child('Вовочка', 4, 3, 3)
mother.add_kinder(kinder)
mother.calm_down(kinder)
mother.feed(kinder)
