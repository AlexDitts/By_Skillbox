import math


class Auto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, way, angle):
        self.y += way * math.sin(angle * math.pi / 180)
        self.x += way * math.cos(angle * math.pi / 180)


class Bus(Auto):
    # TODO: Не хватает метода "войти"  #Метод pass_in_out считает и вошедших и вышедших пассажиров
    def __init__(self, x, y, count=0, cost=25, profit=0): # и на вход принимает соответствующие числа
        super().__init__(x, y)
        self.count = count
        self.cost = cost
        self.profit = profit

    def pass_in_out(self, count_in, count_out):
        """Функция считает количество пассажиров после посадки-высадки. Если пользователь введёт слишком
            большое количество вышедших пассажиров и их количество в автобусе станет ниже 0, ошибка не
            возникает, а количество пассажиров в автобусе становится равным 0"""
        self.count += count_in - count_out
        if self.count < 0:
            self.count = 0

    def move(self, way, angle):
        super().move(way, angle) # На лекции не было такого нужного примера. Я не очень разобрался в
        self.profit += self.count * self.cost * way # работе функции super
        print(self.cost, self.count, way)


bus = Bus(0, 0)
while True:
    course = int(input('Введите направление движения: '))
    distance = int(input('Введите количество километров: '))
    if distance == 0:
        break
    in_pass = int(input('Сколько пассажиров вошло? - '))
    out_pass = int(input('Сколько пассажиров вышло? - '))
    bus.pass_in_out(25, 20)
    bus.move(distance, course)
    print(f'Количество пассажиров после остановки равно: {bus.count}')
    print(f'Стоимость проезда {bus.cost} за один километр пути')
    print(f'Заработано денег {bus.profit} после провоза {bus.count} пассажиров на {distance} километров')
    print(f'Автобус находится в точке с координатами ({bus.x}, {bus.y})')
