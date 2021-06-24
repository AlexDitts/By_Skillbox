def metal_detector(abscissa, ordinate, radius):
    if (abscissa**2 + ordinate**2)**0.5 >= radius:
        print('Монетки рядом нет')
    else:
        print('Монетка где-то рядом')


print('Введите координаты точки:')
x = float(input('х: '))
y = float(input('y: '))
r = float(input('Введите радиус круга: '))

metal_detector(x, y, r)
