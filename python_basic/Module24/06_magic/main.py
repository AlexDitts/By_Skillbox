class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()


class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Mire()
        if isinstance(other, Air):
            return Storm()


class Earth:
    pass


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()


class Steam:

    def __str__(self):
        return 'Steam'


class Lava:

    def __str__(self):
        return 'Лава'

    def __add__(self, other):

        if isinstance(other, Air):
            return FireStorm()


class Lightning:

    def __str__(self):
        return 'Молния'


class Mire:

    def __str__(self):
        return 'Грязь'


class Storm:

    def __str__(self):
        return 'Шторм'


class Dust:

    def __str__(self):
        return 'Пыль'


class FireStorm:

    def __str__(self):
        return 'Огненный шторм'


element_fire = Fire()
element_water = Water()
element_earth = Earth()
element_air = Air()


mix = element_fire + element_earth
print(mix)

mix = element_water + element_fire
print(mix)

mix = element_water + element_earth
print(mix)

mix = element_water + element_air
print(mix)

mix = element_air + element_fire
print(mix)

mix = element_air + element_earth
print(mix)

mix = element_fire + element_earth + element_air
print(mix)
