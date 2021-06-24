import random


class Warrior:
    objects = []
    message = ('Гусеница сбита, движение невозможно!',
               'Повреждён механизм вращения башни. Вращение башни не возможно!',
               'Приборы наблюдения повреждены, дальность обзора снижена!',
               'Мехвод контужен, скорость движения и поворотов снижена!',
               'Орудие повреждено, точность стрельбы снижена!',
               'Повреждение двигателя, скорость движения снижена!',
               'Танк горит!',
               'Повреждена боеукладка, скорость перезарядки снижена!')

    def __init__(self, name, health=100):
        self.health = health
        self.name = name
        Warrior.objects.append(self)

    def __str__(self):
        return f'{self.name}'

   # def __repr__(self):
   #     return f'{self.name}'

    def damage(self):
        self.health -= 20
        print(f'У воина {self.name} осталось {self.health} очков здоровья')
        if self.health <= 0:
            self.is_death()
        else:
            print(f'{random.choice(Warrior.message)}\n')

    def hit(self, unit):
        print(f'{self.name} ударил {unit.name}')
        unit.damage()

    def is_death(self):
        if self.health <= 0:
            print(f'Воин {Warrior.objects.pop(Warrior.objects.index(self))} повержен')
            self.win()

    def win(self):
        # TODO: - Имхо, не очень правильный доступ к победителю.
        #  Если баталию придется расширять на 3 танка и более,
        #  то придется переписывать архитектуру взаимодействия объектов:(
        #  - Но даже если воинов будет больше, в конце останется только один, он и будет в списке под индексом 0.
        #  Если же условия будут у кого больше хп осталось, то это уже совсем другая игра.
        #  Здесь же по условию побеждает тот у кого остались хп.
        #  Если же будет первое второе и третье место, то сделаем сортировку списка воинов по ключу health.
        #  - Суть в том, что если добавить еще несколько воинов,
        #  то согласно данной реализации программы победителем будет не оставшийся в живых,
        #  а тот кто будет первым в списке после того как погибнет первый из войнов
        if len(Warrior.objects) == 1:
            print(f'Победил {Warrior.objects[0].name}')
        else:
            print('в бою остались')
            for warrior in Warrior.objects:
                print(warrior)
            print()


unit1 = Warrior('Scorpion')
unit2 = Warrior('Subzero')
unit3 = Warrior('Lu_Can')
while len(Warrior.objects) > 1:
    partcipiant1 = Warrior.objects[0]
    partcipiant2 = Warrior.objects[1]
    # TODO: А как ударить Лю Каном?:)       # А Лю Каном можно ударить, когда подойдёт его очередь, т.е.
    hit = input('Кто кого бьёт 1 или 2? ')  # когда в первом бою кто-то проиграет. Поскольку наша игра уже
    if hit == '1':                          # давно вышла за рамки ТЗ я взял на себя смелость создать
        partcipiant1.hit(partcipiant2)      # собственные правила игры. Если же у вас есть другие пожелания
    elif hit == '2':                        # то прошу выдать полное ТЗ для этой работы.
        partcipiant2.hit(partcipiant1)      # TODO: Не, всё круто, это был вопрос из любопытства:)
