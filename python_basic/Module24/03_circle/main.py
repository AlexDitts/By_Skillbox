class Circle:

    def __init__(self, x=0, y=0, rad=1):
        self.area = 3.14 * rad**2
        self.circumference = 2 * 3.14 * rad
        self.rad = rad
        self.x = x
        self.y = y

    def intersection(self, unit):
        if ((self.x - unit.x)**2 + (self.y - unit.y)**2)**0.5 < self.rad + unit.rad:
            print('Окружности пересекаются')
            return True
        else:
            print('Окружности не пересекаются')
            return False

    def increase(self, k):
        self.rad *= k


first_circle = Circle(3, 6, 4)
second_circle = Circle(8, 3, 5)
print(first_circle.area)
print(first_circle.circumference)
first_circle.intersection(second_circle)
print(first_circle.rad)
first_circle.increase(3)
print(first_circle.rad)
